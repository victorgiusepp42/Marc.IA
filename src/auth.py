"""
Módulo de autenticação — Google OAuth 2.0 + Flask-Login.

Sprint 3 — implementado em 2026-07-05 conforme plano sequential-coalescing-castle.md.
Decisão: Authlib (OAuth client maduro, suporta Google via OIDC discovery)
         + Flask-Login (sessão, current_user, login_required).

Restrição: apenas contas @discente.ufcat.edu.br (ADR-004). Em dev, pode-se
desabilitar via env var DEV_PERMITIR_LOGIN_LIVRE=1 para testar com Gmail pessoal.
"""

import logging
import os

from authlib.integrations.flask_client import OAuth
from flask import current_app, redirect, request, url_for
from flask_login import LoginManager, current_user, login_user, logout_user

from src.database import db
from src.models_auth import Usuario

logger = logging.getLogger("marcia.auth")

# Singletons — inicializados em init_auth(app)
oauth = OAuth()
login_manager = LoginManager()


def init_auth(app):
    """Inicializa Authlib + Flask-Login na app Flask.

    Chamado UMA VEZ em app.py durante o bootstrap.
    Lê GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, FLASK_SECRET_KEY do ambiente.
    """
    secret_key = os.getenv("FLASK_SECRET_KEY")
    if not secret_key:
        raise RuntimeError(
            "FLASK_SECRET_KEY não definida no .env. "
            "Gere com: python -c \"import secrets; print(secrets.token_hex(32))\""
        )
    app.secret_key = secret_key

    google_client_id = os.getenv("GOOGLE_CLIENT_ID")
    google_client_secret = os.getenv("GOOGLE_CLIENT_KEY") or os.getenv("GOOGLE_CLIENT_SECRET")
    if not google_client_id or not google_client_secret:
        logger.warning(
            "GOOGLE_CLIENT_ID/SECRET não configurados — /auth/login vai falhar. "
            "Veja .env.example."
        )

    oauth.init_app(app)
    # server_metadata_url = descoberta automática via OpenID Connect do Google.
    # Isso evita hardcodar authorize_url, token_url, jwks_uri, etc.
    oauth.register(
        name="google",
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_id=google_client_id,
        client_secret=google_client_secret,
        client_kwargs={"scope": "openid email profile"},
    )

    login_manager.init_app(app)
    # login_view=None: a gente redireciona manualmente no front (splash)
    # pra ter controle sobre a UX (botão grande, sem redirect 302 do Flask-Login).
    login_manager.login_view = None
    # Se a rota exigir login e o usuário não estiver autenticado, retornamos
    # 401 JSON em vez de redirect (porque o front é SPA-like, não tradicional).
    @login_manager.unauthorized_handler
    def _unauthorized():
        if request.path.startswith("/auth/") or request.path == "/auth/me":
            return {"erro": "Não autenticado"}, 401
        # Para /chat/historico e outras APIs, JSON 401
        if request.path.startswith("/chat/") or request.path == "/rota":
            return {"erro": "Não autenticado"}, 401
        # Para /, o frontend vai detectar 401 no /auth/me e mostrar splash
        return {"erro": "Não autenticado"}, 401

    @login_manager.user_loader
    def _load_user(user_id: str):
        """Carrega Usuario pelo PK. user_id vem de User.get_id() = str(self.id)."""
        try:
            uid_int = int(user_id)
        except (TypeError, ValueError):
            return None
        return db.session.get(Usuario, uid_int)


def _email_permitido(email: str) -> bool:
    """Checa se o email está no domínio institucional.

    Em dev com DEV_PERMITIR_LOGIN_LIVRE=1, aceita qualquer email válido
    (útil pra testar antes de configurar test users no Google Cloud).
    """
    if os.getenv("DEV_PERMITIR_LOGIN_LIVRE") == "1":
        return bool(email)
    dominio = os.getenv("DOMINIO_ALUNO", "@discente.ufcat.edu.br")
    return email.lower().endswith(dominio.lower())


def login_via_google():
    """Inicia o fluxo OAuth redirecionando pro Google."""
    redirect_uri = url_for("auth_callback", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


def callback_google():
    """Callback do Google após o usuário autenticar.

    1. Troca o `code` por tokens.
    2. Extrai perfil do id_token (sub, email, name, picture).
    3. Valida domínio institucional.
    4. Cria ou atualiza Usuario no banco.
    5. login_user() cria session cookie.
    6. Redireciona pra /.
    """
    try:
        token = oauth.google.authorize_access_token()
    except Exception as e:
        logger.error("falha ao trocar code por token: %s", e)
        return _erro_oauth("Falha na comunicação com o Google. Tente novamente.")

    # userinfo vem no id_token (campo "userinfo" via claims OIDC)
    userinfo = token.get("userinfo") or token.get("id_token") or {}
    # Fallback: chamada explícita ao endpoint userinfo se necessário
    if not userinfo.get("sub"):
        try:
            resp = oauth.google.get("userinfo", token=token)
            userinfo = resp.json()
        except Exception as e:
            logger.error("falha ao buscar userinfo: %s", e)
            return _erro_oauth("Não foi possível obter seus dados do Google.")

    google_id = userinfo.get("sub")
    email = (userinfo.get("email") or "").lower()
    nome = userinfo.get("name") or email.split("@")[0]
    foto_url = userinfo.get("picture")

    if not google_id or not email:
        logger.error("userinfo incompleto: %s", userinfo)
        return _erro_oauth("Conta Google sem dados essenciais (id/email).")

    if not _email_permitido(email):
        dominio = os.getenv("DOMINIO_ALUNO", "@discente.ufcat.edu.br")
        logger.warning("login recusado — email fora do domínio: %s", email)
        return _erro_oauth(
            f"Acesso restrito a alunos UFCAT ({dominio}). "
            f"Sua conta ({email}) não se qualifica."
        )

    # Upsert no banco
    usuario = db.session.query(Usuario).filter_by(google_id=google_id).first()
    if usuario is None:
        # Também checa se já existe com esse email (improvável mas defensivo)
        usuario_existente = db.session.query(Usuario).filter_by(email=email).first()
        if usuario_existente is not None:
            # Vincula o google_id a um usuario criado por outro caminho
            usuario_existente.google_id = google_id
            usuario = usuario_existente

    if usuario is None:
        usuario = Usuario(
            google_id=google_id,
            email=email,
            nome=nome,
            foto_url=foto_url,
        )
        db.session.add(usuario)
        logger.info("novo usuario criado: %s", email)
    else:
        # Atualiza nome/foto (podem mudar no Google)
        usuario.nome = nome
        if foto_url:
            usuario.foto_url = foto_url
        logger.info("login de usuario existente: %s", email)

    db.session.commit()
    login_user(usuario, remember=True)
    return redirect(url_for("index"))


def logout():
    """Encerra a sessão e redireciona pra /."""
    if current_user.is_authenticated:
        logger.info("logout: %s", current_user.email)
    logout_user()
    return redirect(url_for("index"))


def dev_auto_login():
    """Cria/loga um usuário fake pra rodar local sem OAuth.

    Só funciona se DEV_AUTO_LOGIN=1 estiver no ambiente. Em prod
    (sem essa var) retorna 403. Útil pra Victor testar enquanto
    não tem as credenciais Google configuradas.
    """
    if os.getenv("DEV_AUTO_LOGIN") != "1":
        return {"erro": "DEV_AUTO_LOGIN não habilitado"}, 403

    email = "dev@localhost"
    google_id = "dev-local-" + os.urandom(4).hex()
    usuario = db.session.query(Usuario).filter_by(email=email).first()
    if usuario is None:
        usuario = Usuario(
            google_id=google_id,
            email=email,
            nome="Victor (dev)",
            foto_url=None,
        )
        db.session.add(usuario)
        db.session.commit()
        logger.info("dev_auto_login: usuario dev criado")
    login_user(usuario, remember=True)
    return redirect(url_for("index"))


def _erro_oauth(mensagem: str):
    """Helper para retornar erro de OAuth pro usuário sem quebrar o fluxo.

    Em produção renderizaríamos uma página de erro; aqui redirecionamos pra /
    com um query param que o front pode ler. Como ainda não temos flash messages,
    logamos e mandamos pro index — front pode mostrar um alert via location.hash.
    """
    from urllib.parse import quote
    return redirect(f"/?auth_error={quote(mensagem)}")