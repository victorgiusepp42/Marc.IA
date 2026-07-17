"""
app.py — Ponto de entrada do Marc.IA
Servidor Flask que conecta interface web ao agente tutor via API Claude.
"""

import json
import logging
import os
import sys
import time
import traceback

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

from src.database import db
from src.models import Sessao, LogExecucao, LogErro, Feedback, Metrica
from src.agente_ip import AgenteIP
from src import auth as auth_module
from flask_login import login_required, current_user

# === Logging estruturado ===
# Saída em stderr (capturado por Flask/terminal) com formato timestampado.
# Permite debug eficiente e observabilidade em produção.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("marcia")

# Carrega variáveis de ambiente (.env)
load_dotenv()

# Inicializa Flask
app = Flask(__name__)

# === ProxyFix ===
# Railway (e qualquer PaaS) termina TLS no proxy de borda e repassa a
# requisição pro container via HTTP interno. Sem ProxyFix, o Flask não
# sabe que a conexão ORIGINAL do usuário era HTTPS — e gera URLs
# internas como http://, o que quebra o OAuth do Google (recusa
# redirect_uri HTTP fora de localhost).
#
# x_proto=2: confia até em 2 hops de X-Forwarded-Proto (edge + interno
# do Railway; em testes x_proto=1 não pegava)
# x_host=2:  idem pra X-Forwarded-Host
# x_for=1:   confia em 1 hop de X-Forwarded-For (preserva IP do cliente)
#
# Em dev local (sem proxy) esses headers não existem → comportamento
# padrão (http://127.0.0.1:5000) continua igual.
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=2, x_host=2, x_for=1)

# === Configuração dos bancos de dados ===
# Banco principal: marcia.db (sessoes, perfis de aluno)
# Banco de logs: logs.db (execucoes, erros) — engine separado via BIND_KEYS
#   Vantagem: queries de log não competem com queries de aluno
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# === Banco de dados ===
# Prioriza DATABASE_URL quando setada (produção: Postgres do Railway).
# Fallback pra SQLite local quando não tem (dev local do Victor).
# Em prod Railway, DATABASE_URL vem injetada automaticamente como referência
# ${{ Postgres.DATABASE_URL }} — nesse caso a engine SESSION é Postgres.
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    # Railway injeta "postgres://" mas SQLAlchemy 2.x prefere "postgresql://"
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    # Em prod usamos o MESMO banco pra logs (bind_key aponta pra mesma engine)
    app.config["SQLALCHEMY_BINDS"] = {
        "logs": DATABASE_URL,
    }
else:
    # Dev local: SQLite com fallback pros 2 arquivos (sessoes + logs separados)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATA_DIR}/marcia.db"
    app.config["SQLALCHEMY_BINDS"] = {
        "logs": f"sqlite:///{DATA_DIR}/logs.db",
    }
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa SQLAlchemy com a app
db.init_app(app)

# Cria tabelas se não existirem (em ambos os engines)
with app.app_context():
    db.create_all()  # engine principal (sessoes, usuarios, perfil)
    db.create_all(bind_key="logs")  # engine de logs (execucoes, erros)

    # === Migrations manuais (substituem Alembic até a E3) ===
    # Adiciona colunas novas em tabelas existentes. Execute é idempotente
    # (try/except) — se a coluna já existe, sqlite levanta OperationalError
    # e a gente ignora. Se não existe, cria com default seguro.
    # Padrão inspirado na lição "schema migration sem Alembic" do sprint.
    try:
        db.session.execute(db.text(
            "ALTER TABLE sessoes ADD COLUMN historico_por_topico_json TEXT DEFAULT '{}'"
        ))
        db.session.commit()
        logger.info("migration: coluna historico_por_topico_json adicionada em sessoes")
    except Exception as e:
        # Provavelmente "duplicate column name" — já existe, ignora
        db.session.rollback()
        logger.debug("migration historico_por_topico_json: %s (provavelmente já existe)", e)

# Inicializa Authlib + Flask-Login (lê FLASK_SECRET_KEY, GOOGLE_CLIENT_ID/SECRET)
auth_module.init_auth(app)

# Instância global do agente (singleton — só temos 1 disciplina na Sprint 1)
agente = AgenteIP()

# === Detecção de modo dev/prod (auditoria segurança 1.3) ===
# True quando FLASK_DEBUG=1 ou FLASK_ENV=development — usado para
# habilitar fallbacks locais (ex: ADMIN_TOKEN dev) que NUNCA devem
# rodar em produção.
DEBUG_MODE = os.getenv("FLASK_DEBUG", "0") == "1" or os.getenv("FLASK_ENV", "") == "development"

# Aviso de segurança do admin (auditoria 1.3)
# Sem este log, deploy em prod sem ADMIN_TOKEN passaria silencioso
# (dev fallback aceitaria "dev-token-marc-IA" sem ninguém saber).
if DEBUG_MODE and not os.getenv("ADMIN_TOKEN"):
    logger.warning("[ADMIN] MODO DEV ativo: /admin/logs aceita 'dev-token-marc-IA' como fallback")
elif not DEBUG_MODE and not os.getenv("ADMIN_TOKEN"):
    logger.error("[ADMIN] MODO PROD sem ADMIN_TOKEN — /admin/logs vai retornar 503")

# Tamanho máximo da mensagem do aluno (caracteres)
MAX_MENSAGEM = 2000

# Tamanho máximo do bloco de código enviado (caracteres)
MAX_CODIGO = 8000

# Linguagens aceitas no campo de código
LINGUAGENS_ACEITAS = {"python", "portugol"}

# Tamanho máximo da resposta a um exercício (caracteres) — maior que MAX_MENSAGEM
# porque o aluno pode colar um bloco inteiro de portugol/python.
MAX_RESPOSTA_EX = 4000

# Modo dev: auto-login + pulo de OAuth. Em produção deve ficar DESLIGADO (=0).
# Quando =1, libera /chat-direct e exibe toggles "dev" nos templates.
# Default: False quando a env var não está setada — fail-safe pra prod.
DEV_AUTO_LOGIN = os.getenv("DEV_AUTO_LOGIN") == "1"


# === Helpers compartilhados entre rotas ===
# Refator 2026-07-08: eliminam duplicação de (a) resolução de identidade
# do usuário logado/anon e (b) bloco try/except LogErro em rotas POST/GET.


def _resolver_uid(fonte=None):
    """Resolve usuário: usa current_user.email se autenticado, senão busca
    usuario_id no dict do body (POST) ou request.args (GET)."""
    if current_user.is_authenticated:
        return current_user.email
    if fonte is None:
        fonte = request.args
    if isinstance(fonte, dict):
        raw = fonte.get("usuario_id", "")
    else:
        raw = str(fonte) if fonte else ""
    return str(raw).strip() or "anonimo"


def _log_erro(endpoint, e, usuario_id="anonimo", contexto=None):
    """Persiste LogErro no bind 'logs'. Try/except aninhado — nunca propaga
    falha de log pra cima (não pode quebrar ainda mais a resposta da rota)."""
    try:
        log = LogErro(
            usuario_id=usuario_id,
            endpoint=endpoint,
            erro_tipo=type(e).__name__,
            erro_mensagem=str(e)[:500],
            traceback=traceback.format_exc()[:5000],
            contexto_json=json.dumps(contexto) if contexto else None,
        )
        db.session.add(log)
        db.session.commit()
    except Exception:
        db.session.rollback()


@app.route("/")
def index():
    """Serve a página principal.

    Logado → tutor (chat.html). Não logado → splash (splash.html).
    Em modo dev (DEV_AUTO_LOGIN=1), sempre mostra o tutor.
    """
    # Modo dev: pula direto pro tutor sem login (usado pelo Diogo no fluxo de prototipagem)
    if DEV_AUTO_LOGIN:
        return render_template(
            "chat.html",
            dev_mode=DEV_AUTO_LOGIN,
            current_user=current_user,
        )

    if current_user.is_authenticated:
        return render_template(
            "chat.html",
            dev_mode=DEV_AUTO_LOGIN,
            current_user=current_user,
        )
    return render_template("splash.html", dev_mode=DEV_AUTO_LOGIN, current_user=current_user)


@app.route("/chat-direct")
def chat_direct():
    """DEV ONLY: abre o tutor sem precisar de login.

    Existe enquanto não temos OAuth configurado no ambiente.
    Quando o Google OAuth entrar em produção, remova esta rota.

    Gate de segurança: se DEV_AUTO_LOGIN != "1", retorna 404 pra que
    a rota não exista em produção (mesmo que o decorator continue
    registrado — fail-safe: rota existe mas responde 404).
    """
    if not DEV_AUTO_LOGIN:
        return jsonify({"erro": "Not Found"}), 404
    return render_template("chat.html", dev_mode=DEV_AUTO_LOGIN, current_user=current_user)


@app.route("/health", methods=["GET"])
def health():
    """Health check simples pro watchdog (público, sem auth)."""
    return jsonify({"status": "ok"}), 200


# === Rotas de autenticação ===
@app.route("/auth/login", methods=["GET"])
def auth_login():
    """Inicia fluxo OAuth redirecionando pro Google.

    Se DEV_AUTO_LOGIN=1, loga com usuário fake direto (sem Google).
    """
    if os.getenv("DEV_AUTO_LOGIN") == "1":
        return auth_module.dev_auto_login()
    return auth_module.login_via_google()


@app.route("/auth/callback", methods=["GET"])
def auth_callback():
    """Callback do Google — cria/atualiza usuário, abre sessão."""
    return auth_module.callback_google()


@app.route("/auth/logout", methods=["GET"])
@login_required
def auth_logout():
    """Encerra sessão e volta pro splash."""
    return auth_module.logout()


@app.route("/auth/me", methods=["GET"])
def auth_me():
    """Retorna info do usuário logado ou 401.

    O frontend usa isso pra decidir se mostra splash de login
    ou carrega o chat. Resposta:
      200: {logado: true, usuario: {id, email, nome, foto_url}}
      401: {logado: false}

    Modo dev: se DEV_AUTO_LOGIN=1 no ambiente, retorna um usuário fake
    sem precisar de OAuth. Útil pra testar local sem configurar Google Cloud.
    """
    # Modo dev — login automático com usuário fake
    if os.getenv("DEV_AUTO_LOGIN") == "1":
        return jsonify({
            "logado": True,
            "usuario": {
                "id": 0,
                "email": "dev@localhost",
                "nome": "Victor (dev)",
                "foto_url": None,
            },
        })
    if not current_user.is_authenticated:
        return jsonify({"logado": False}), 401
    return jsonify({
        "logado": True,
        "usuario": {
            "id": current_user.id,
            "email": current_user.email,
            "nome": current_user.nome,
            "foto_url": current_user.foto_url,
        },
    })


@app.route("/chat/historico", methods=["GET"])
def chat_historico():
    """Retorna o histórico persistido da sessão.

    Se o aluno estiver logado, usa o email como chave. Senão, usa o
    usuario_id da query string (UUID antigo) — fallback pra manter
    compatibilidade com a versão pré-auth.
    """
    uid = _resolver_uid()
    try:
        sessao = Sessao.carregar_ou_criar(uid)
        return jsonify({
            "mensagens": sessao.historico,
        })
    except Exception as e:
        logger.error(
            "chat_historico FAILED: usuario=%s erro=%s",
            uid, e, exc_info=True,
        )
        _log_erro("/chat/historico", e, usuario_id=uid)
        return jsonify({"erro": "Erro interno do servidor. Tente novamente."}), 500


@app.route("/rota", methods=["GET"])
def rota():
    """Retorna o plano de tópicos da disciplina + estado atual (tópico + linguagem)."""
    caminho = os.path.join("data", "plano.json")
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            plano = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({"erro": "Plano de ensino não encontrado."}), 404

    # Inclui estado atual da sessão pra o front saber o que tá selecionado
    estado = {}
    uid = _resolver_uid()
    sessao = Sessao.carregar_ou_criar(uid)
    if sessao.topico_ativo:
        estado["topico_ativo"] = sessao.topico_ativo
    if sessao.linguagem_topico:
        estado["linguagem_topico"] = sessao.linguagem_topico

    return jsonify({**plano, "estado": estado})


@app.route("/rota/selecionar", methods=["POST"])
def rota_selecionar():
    """Atualiza tópico ativo + linguagem escolhida.

    Body JSON:
      {
        "topico_id": "alg-variaveis",
        "linguagem": "portugol" | "visualg" | "python"
      }

    Para tópicos com `linguagem_obrigatoria` (ex: recursao = portugol),
    ignora o valor enviado e usa o obrigatório.
    """
    dados = request.get_json(force=True, silent=True)
    if not dados or not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido."}), 400

    topico_id = str(dados.get("topico_id", "")).strip()
    linguagem = str(dados.get("linguagem", "")).strip().lower()
    if not topico_id:
        return jsonify({"erro": "topico_id obrigatório."}), 400

    # Carrega plano pra validar e checar linguagem obrigatória
    caminho = os.path.join("data", "plano.json")
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            plano = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({"erro": "Plano não encontrado."}), 500

    topico = next((t for t in plano.get("topicos", []) if t["id"] == topico_id), None)
    if topico is None:
        return jsonify({"erro": f"Tópico '{topico_id}' não existe."}), 404

    # Se tem linguagem obrigatória, força
    obrigatoria = topico.get("linguagem_obrigatoria")
    if obrigatoria:
        linguagem = obrigatoria

    # Se não veio linguagem mas o tópico aceita só uma, usa a única
    if not linguagem:
        linguagens_aceitas = topico.get("linguagens_aceitas", [])
        if len(linguagens_aceitas) == 1:
            linguagem = linguagens_aceitas[0]

    # Valida que linguagem tá nas linguagens_aceitas
    if linguagem not in topico.get("linguagens_aceitas", []):
        return jsonify({
            "erro": f"Linguagem '{linguagem}' não aceita pro tópico '{topico_id}'. "
                    f"Aceitas: {topico.get('linguagens_aceitas', [])}."
        }), 400

    # Identifica o usuário (logado ou anônimo)
    uid = _resolver_uid(dados)

    sessao = Sessao.carregar_ou_criar(uid)
    sessao.topico_ativo = topico_id
    sessao.linguagem_topico = linguagem
    sessao.salvar()

    # Log de execução — try/except aninhado pra não quebrar o salvamento
    try:
        log = LogExecucao(
            usuario_id=uid,
            mensagem_chars=0,
            codigo_chars=0,
            linguagem=linguagem,
            complexidade="baixa",
            tier="selecionar-topico",
            perfil_topico=topico_id,
            perfil_preferencias=0,
            perfil_topicos_explicados=0,
            duracao_ms=0,
            kb_chunks_usados=0,
        )
        db.session.add(log)
        db.session.commit()
    except Exception as log_err:
        # Log de log falhou — não pode quebrar a resposta
        logger.error("falha ao gravar LogExecucao (rota/selecionar): %s", log_err)
        db.session.rollback()

    return jsonify({
        "topico_ativo": sessao.topico_ativo,
        "linguagem_topico": sessao.linguagem_topico,
    })


def _montar_conteudo_aluno(mensagem: str, codigo: str, linguagem: str) -> str:
    """Monta o conteúdo enviado ao tutor combinando pergunta do aluno e bloco de código.

    Quando há código, o tutor recebe um envelope estruturado em vez de texto colado.
    Preserva indentação (4 espaços dentro do bloco) para o code tracing funcionar.
    """
    if codigo:
        # Sanitiza linguagem para o subconjunto aceito; default python
        lang = linguagem if linguagem in LINGUAGENS_ACEITAS else "python"
        bloco = (
            f"```\n"
            f"# LINGUAGEM: {lang}\n"
            f"# --- CÓDIGO DO ALUNO ---\n"
            f"{codigo}\n"
            f"# --- FIM DO CÓDIGO ---\n"
            f"```"
        )
        if mensagem:
            return f"{bloco}\n\n[PERGUNTA DO ALUNO]\n{mensagem}"
        return f"{bloco}\n\n[O ALUNO PEDIU ANÁLISE DO CÓDIGO ACIMA. FAÇA CODE TRACING E IDENTIFIQUE ERROS/IDEIAS.]"
    return mensagem


@app.route("/chat", methods=["POST"])
def chat():
    """Recebe mensagem do aluno, processa via agente e retorna resposta.

    Identidade: se logado, usa email do current_user. Senão, usa o
    usuario_id do body (UUID anônimo) — fallback pra sessão pré-auth.

    Instrumentação:
      - Cada sucesso → 1 INSERT em data/logs.db (tabela execucoes)
      - Cada erro → 1 INSERT em data/logs.db (tabela erros)
      - Logs de erro nunca quebram a resposta 500 (try/except aninhado)
    """
    inicio = time.time()
    # Tenta parsear JSON — protege contra body inválido
    # force=True aceita JSON mesmo sem Content-Type exato (cobre integrações e navegador)
    dados = request.get_json(force=True, silent=True)

    if not dados or not isinstance(dados, dict):
        return jsonify({"erro": "Corpo da requisição precisa ser JSON válido em UTF-8."}), 400

    mensagem = str(dados.get("mensagem", "")).strip()
    codigo = str(dados.get("codigo", "")).strip()
    linguagem = str(dados.get("linguagem", "python")).strip().lower()
    # Identidade: prioriza usuário logado; senão usa o do body (modo anônimo)
    usuario_id = _resolver_uid(dados)

    # Validações de input — aluno precisa mandar pelo menos mensagem OU código
    if not mensagem and not codigo:
        return jsonify({"erro": "Envie uma dúvida ou um código para análise."}), 400

    if len(mensagem) > MAX_MENSAGEM:
        return jsonify({"erro": f"Mensagem muito longa (máx {MAX_MENSAGEM} caracteres)."}), 400

    if len(codigo) > MAX_CODIGO:
        return jsonify({"erro": f"Código muito longo (máx {MAX_CODIGO} caracteres)."}), 400

    if linguagem not in LINGUAGENS_ACEITAS:
        linguagem = "python"

    if not usuario_id:
        usuario_id = "anonimo"

    # Monta o conteúdo estruturado que vai pro tutor
    conteudo_aluno = _montar_conteudo_aluno(mensagem, codigo, linguagem)

    logger.info(
        "chat request: usuario=%s mensagem=%dchars codigo=%dchars linguagem=%s",
        usuario_id, len(mensagem), len(codigo), linguagem,
    )

    try:
        # Carrega ou cria sessão do aluno (SQLAlchemy)
        sessao = Sessao.carregar_ou_criar(usuario_id)

        # Gera resposta do tutor (retorna tupla (texto, tier_label))
        resposta, tier_label = agente.responder(conteudo_aluno, sessao)

        # Atualiza sessão: histórico sequencial (legado, mantido p/ compatibilidade)
        sessao.adicionar_mensagem("user", conteudo_aluno)
        sessao.adicionar_mensagem("assistant", resposta)

        # === NOVO: histórico segregado por tópico ===
        # Permite ao aluno reabrir a conversa salva de qualquer aula
        # da trilha. Se não tem topico_ativo, não persiste por tópico.
        if sessao.topico_ativo:
            sessao.adicionar_mensagem_topico("user", conteudo_aluno, sessao.topico_ativo)
            sessao.adicionar_mensagem_topico("assistant", resposta, sessao.topico_ativo)
        sessao.salvar()

        # Grava log de execução em data/logs.db (engine separado)
        agente_log = agente.ultimo_log
        try:
            log = LogExecucao(
                usuario_id=usuario_id,
                mensagem_chars=len(mensagem),
                codigo_chars=len(codigo),
                linguagem=linguagem,
                complexidade=agente_log.get("complexidade"),
                tier=tier_label,
                perfil_topico=agente_log.get("perfil_topico"),
                perfil_preferencias=agente_log.get("qtd_prefs", 0),
                perfil_topicos_explicados=agente_log.get("qtd_topicos", 0),
                duracao_ms=int((time.time() - inicio) * 1000),
                kb_chunks_usados=len(agente_log.get("chunks") or []),
            )
            db.session.add(log)
            db.session.commit()
        except Exception as log_err:
            # Log de log falhou — não pode quebrar a resposta
            logger.error("falha ao gravar LogExecucao: %s", log_err)
            db.session.rollback()

        logger.info(
            "chat ok: usuario=%s tier=%s",
            usuario_id, tier_label,
        )

        return jsonify({
            "resposta": resposta,
            "tier": tier_label,
        })

    except Exception as e:
        # Log estruturado com traceback completo pra debug eficiente
        logger.error(
            "chat FAILED: usuario=%s erro=%s",
            usuario_id, e, exc_info=True,
        )
        _log_erro("/chat", e, usuario_id=usuario_id, contexto={
            "msg_chars": len(mensagem),
            "codigo_chars": len(codigo),
            "linguagem": linguagem,
        })
        # Catch-all — nunca retorna 500 sem JSON para o front
        return jsonify({
            "erro": "Erro interno do servidor. Tente novamente."
        }), 500


# === EXERCÍCIOS INLINE (FRO-05) ===
# Esqueleto adicionado em 2026-07-08. Validação por similaridade de keywords
# (sem execução real de portugol/python) — ver src/exercicios.py pra detalhes.


@app.route("/exercicio/listar", methods=["GET"])
def exercicio_listar():
    """Lista exercícios (opcionalmente filtrados por topico_id).

    Devolve apenas campos públicos — `gabarito_completo` e
    `gabarito_resumo` ficam escondidos até o aluno enviar a resposta
    ou pedir explicitamente (esqueleto: gabarito vem no POST validar).
    """
    topico_id = request.args.get("topico_id", "").strip() or None
    usuario_id = _resolver_uid()
    try:
        from src import exercicios as ex_mod
        itens = ex_mod.listar(topico_id=topico_id)
        publicos = [{
            "id": e["id"],
            "topico_id": e["topico_id"],
            "lista_origem": e["lista_origem"],
            "numero": e["numero"],
            "titulo": e["titulo"],
            "enunciado": e["enunciado"],
            "linguagem": e["linguagem"],
            "entrada_exemplo": e["entrada_exemplo"],
            "saida_esperada": e["saida_esperada"],
        } for e in itens]
        return jsonify({"exercicios": publicos})
    except Exception as e:
        logger.error(
            "exercicio_listar FAILED: usuario=%s topico=%s erro=%s",
            usuario_id, topico_id, e, exc_info=True,
        )
        _log_erro("/exercicio/listar", e, usuario_id=usuario_id, contexto={"topico_id": topico_id})
        return jsonify({"erro": "Erro interno ao listar exercícios."}), 500


@app.route("/exercicio/validar", methods=["POST"])
def exercicio_validar():
    """Valida resposta de um exercício. Retorna JSON com correta/score/feedback/gabarito.

    Log em LogExecucao com `tier="validar-exercicio"` e `perfil_topico=exercicio_id`
    (não cria tabela nova — reaproveita schema existente).
    """
    inicio = time.time()
    dados = request.get_json(force=True, silent=True)
    if not dados or not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido."}), 400

    exercicio_id = str(dados.get("exercicio_id", "")).strip()
    resposta = str(dados.get("resposta", ""))
    if not exercicio_id:
        return jsonify({"erro": "exercicio_id obrigatório."}), 400
    if len(resposta) > MAX_RESPOSTA_EX:
        return jsonify({
            "erro": f"Resposta muito longa (máx {MAX_RESPOSTA_EX} caracteres)."
        }), 400

    usuario_id = _resolver_uid(dados)

    try:
        from src import exercicios as ex_mod
        correta, score, feedback, gabarito = ex_mod.validar(exercicio_id, resposta)

        try:
            log = LogExecucao(
                usuario_id=usuario_id,
                mensagem_chars=len(resposta),
                codigo_chars=0,
                linguagem="",
                complexidade="baixa",
                tier="validar-exercicio",
                perfil_topico=exercicio_id,
                perfil_preferencias=0,
                perfil_topicos_explicados=0,
                duracao_ms=int((time.time() - inicio) * 1000),
                kb_chunks_usados=0,
            )
            db.session.add(log)
            db.session.commit()
        except Exception as log_err:
            logger.error("falha ao gravar LogExecucao (exercicio): %s", log_err)
            db.session.rollback()

        return jsonify({
            "correta": correta,
            "score": score,
            "feedback": feedback,
            "gabarito": gabarito,
        })

    except Exception as e:
        logger.error(
            "exercicio_validar FAILED: usuario=%s erro=%s",
            usuario_id, e, exc_info=True,
        )
        _log_erro("/exercicio/validar", e, usuario_id=usuario_id, contexto={"exercicio_id": exercicio_id})
        return jsonify({"erro": "Erro interno ao validar exercício."}), 500


# === FEEDBACK + NPS (FRO-06 / MET-01 / MET-02) ===
# Adicionado em 2026-07-08. Métricas de qualidade do tutor + satisfação do aluno.
# Persiste em data/logs.db (bind "logs"), tabelas `feedbacks` e `metricas`.


@app.route("/feedback", methods=["POST"])
def feedback_salvar():
    """Registra like/dislike em uma resposta do tutor.

    Body JSON:
      {
        "mensagem_idx": 3,            # índice da resposta em Sessao.historico
        "tipo": "like" | "dislike",
        "topico_id": "py-variaveis",  # opcional, default null
        "sessao_id": 7                # opcional — id numérico da Sessao
      }
    """
    dados = request.get_json(force=True, silent=True)
    if not dados or not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido."}), 400

    mensagem_idx = dados.get("mensagem_idx")
    tipo = str(dados.get("tipo", "")).strip().lower()
    if not isinstance(mensagem_idx, int) or mensagem_idx < 0:
        return jsonify({"erro": "mensagem_idx deve ser int >= 0."}), 400
    if tipo not in ("like", "dislike"):
        return jsonify({"erro": "tipo deve ser 'like' ou 'dislike'."}), 400

    usuario_id = _resolver_uid(dados)

    topico_id = str(dados.get("topico_id", "")).strip() or None
    sessao_id = dados.get("sessao_id")  # opcional
    if sessao_id is not None and not isinstance(sessao_id, int):
        sessao_id = None

    try:
        fb = Feedback(
            usuario_id=usuario_id,
            sessao_id=sessao_id,
            topico_id=topico_id,
            mensagem_idx=mensagem_idx,
            tipo=tipo,
        )
        db.session.add(fb)
        db.session.commit()
        return jsonify({"ok": True, "id": fb.id})
    except Exception as e:
        logger.error("feedback_salvar FAILED: usuario=%s erro=%s", usuario_id, e, exc_info=True)
        db.session.rollback()
        _log_erro("/feedback", e, usuario_id=usuario_id)
        return jsonify({"erro": "Erro ao salvar feedback."}), 500


@app.route("/metricas", methods=["POST"])
def metricas_salvar():
    """Registra NPS ou Sean Ellis.

    Body JSON:
      {
        "tipo": "nps" | "sean_ellis",
        "valor": 9                       # int 0-10 (nps) | string (sean_ellis)
      }
    """
    dados = request.get_json(force=True, silent=True)
    if not dados or not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido."}), 400

    tipo = str(dados.get("tipo", "")).strip().lower()
    valor = dados.get("valor")
    if tipo not in ("nps", "sean_ellis"):
        return jsonify({"erro": "tipo deve ser 'nps' ou 'sean_ellis'."}), 400

    # Validação do valor conforme o tipo
    if tipo == "nps":
        if not isinstance(valor, int) or valor < 0 or valor > 10:
            return jsonify({"erro": "NPS deve ser int entre 0 e 10."}), 400
        valor_str = str(valor)
    else:  # sean_ellis
        if valor not in ("muito", "um_pouco", "indiferente"):
            return jsonify({"erro": "Sean Ellis valor inválido."}), 400
        valor_str = valor

    usuario_id = _resolver_uid(dados)

    try:
        m = Metrica(usuario_id=usuario_id, tipo=tipo, valor=valor_str)
        db.session.add(m)
        db.session.commit()
        return jsonify({"ok": True, "id": m.id})
    except Exception as e:
        logger.error("metricas_salvar FAILED: usuario=%s erro=%s", usuario_id, e, exc_info=True)
        db.session.rollback()
        _log_erro("/metricas", e, usuario_id=usuario_id)
        return jsonify({"erro": "Erro ao salvar métrica."}), 500


@app.route("/metricas/contadores", methods=["GET"])
def metricas_contadores():
    """Retorna o total de métricas por tipo (debug/inspeção).

    Útil pra validar a integração sem precisar abrir o SQLite.
    """
    try:
        contadores = {}
        for tipo in ("nps", "sean_ellis"):
            contadores[tipo] = Metrica.query.filter_by(tipo=tipo).count()
        contadores["feedbacks_like"] = Feedback.query.filter_by(tipo="like").count()
        contadores["feedbacks_dislike"] = Feedback.query.filter_by(tipo="dislike").count()
        return jsonify(contadores)
    except Exception as e:
        logger.error("metricas_contadores FAILED: %s", e, exc_info=True)
        return jsonify({"erro": "Erro ao buscar contadores."}), 500


# === HISTÓRICO POR TÓPICO (persistência navegável) ===
# Adicionado em 2026-07-08. Permite ao aluno reabrir conversas salvas
# de qualquer tópico da trilha. Cada tópico mantém sua própria lista
# de mensagens (par user/assistant), separada do histórico sequencial
# legado em `sessoes.historico_json`.


@app.route("/sessao/topico/<topico_id>", methods=["GET"])
def sessao_topico(topico_id):
    """Retorna histórico salvo de um tópico específico do aluno.

    Query string: ?usuario_id=X (opcional se logado)
    Response:
      {
        "topico_id": "...",
        "mensagens": [{"role": "user"|"assistant", "content": "...", "timestamp": "..."}, ...],
        "total": N
      }
    """
    topico_id = topico_id.strip()
    if not topico_id:
        return jsonify({"erro": "topico_id obrigatório."}), 400

    usuario_id = _resolver_uid()

    try:
        sessao = Sessao.carregar_ou_criar(usuario_id)
        msgs = sessao.historico_topico(topico_id)
        return jsonify({
            "topico_id": topico_id,
            "mensagens": msgs,
            "total": len(msgs),
        })
    except Exception as e:
        logger.error("sessao_topico FAILED: usuario=%s topico=%s erro=%s",
                     usuario_id, topico_id, e, exc_info=True)
        db.session.rollback()
        _log_erro(f"/sessao/topico/{topico_id}", e, usuario_id=usuario_id)
        return jsonify({"erro": "Erro ao buscar histórico do tópico."}), 500


@app.route("/sessao/topicos", methods=["GET"])
def sessao_topicos_lista():
    """Lista tópicos do aluno que têm histórico salvo.

    Retorna lista ordenada do mais recente pro mais antigo:
      [{"topico_id": "...", "qtd_mensagens": N, "ultimo_timestamp": "..."}, ...]
    """
    usuario_id = _resolver_uid()

    try:
        sessao = Sessao.carregar_ou_criar(usuario_id)
        topicos = sessao.listar_topicos_com_historico()
        return jsonify({"topicos": topicos, "total": len(topicos)})
    except Exception as e:
        logger.error("sessao_topicos_lista FAILED: %s", e, exc_info=True)
        _log_erro("/sessao/topicos", e, usuario_id=usuario_id)
        return jsonify({"erro": "Erro ao listar tópicos com histórico."}), 500


# === ADMIN — endpoint de auditoria ===
# Adicionado em 2026-07-08. Acesso controlado por ADMIN_TOKEN em .env.
# Em dev/teste, ADMIN_TOKEN vazio = desabilitado. Em prod, sempre setar
# um token forte (random 32+ chars). Sem token, retorna 503.


def _admin_authorized() -> bool:
    """Verifica header X-Admin-Token contra ADMIN_TOKEN do ambiente.

    Em DEV (DEBUG_MODE=True): aceita "dev-token-marc-IA" como fallback.
    Em PROD (DEBUG_MODE=False): ADMIN_TOKEN obrigatório, sem fallback.
    """
    expected = os.getenv("ADMIN_TOKEN", "")
    if not expected:
        if DEBUG_MODE:
            return request.headers.get("X-Admin-Token", "") == "dev-token-marc-IA"
        return False
    return request.headers.get("X-Admin-Token", "") == expected


@app.route("/admin/logs", methods=["GET"])
def admin_logs():
    """Auditoria cross-tabela. Suporta:

      ?tipo=execucoes|feedbacks|metricas|erros   (default = todos + agregado)
      ?usuario=substring                           (filtra por usuario_id)
      ?desde=YYYY-MM-DD                           (a partir de)
      ?limite=N                                   (default 50, max 500)

    Header obrigatório: X-Admin-Token: <ADMIN_TOKEN>
    Em dev sem ADMIN_TOKEN setado: usa "dev-token-marc-IA" como fallback.
    Em prod: defina ADMIN_TOKEN=seu_token_secreto (32+ chars).
    """
    if not _admin_authorized():
        return jsonify({"erro": "Não autorizado."}), 401

    tipo = request.args.get("tipo", "").strip().lower()
    usuario_filtro = request.args.get("usuario", "").strip()
    desde_str = request.args.get("desde", "").strip()
    try:
        limite = max(1, min(int(request.args.get("limite", "50")), 500))
    except ValueError:
        limite = 50

    # Valida 'desde' (formato YYYY-MM-DD) — se inválido, ignora
    desde_iso = ""
    if desde_str:
        try:
            from datetime import datetime, timezone
            dt = datetime.fromisoformat(desde_str).replace(tzinfo=timezone.utc)
            desde_iso = dt.isoformat()
        except ValueError:
            pass

    resultado = {}
    tabelas = [tipo] if tipo in ("execucoes", "feedbacks", "metricas", "erros") else \
              ["execucoes", "feedbacks", "metricas", "erros"]

    try:
        # Acessa direto via SQLAlchemy ORM. As 4 tabelas administrativas
        # (execucoes|feedbacks|metricas|erros) estão no bind "logs".
        # SQLAlchemy 2.0: o .query do model sem engine certo vai usar a
        # engine principal. Pra forçar a engine do bind "logs", uso
        # `db.session.query(...).with_statement_hint(...)` ou o jeito
        # mais simples: uma Session específica do engine "logs".
        tabela_para_modelo = {
            "execucoes": LogExecucao,
            "feedbacks": Feedback,
            "metricas": Metrica,
            "erros": LogErro,
        }

        # Session fixa apontando pro engine "logs".
        from sqlalchemy.orm import sessionmaker
        engine_logs = db.get_engine(app=app, bind="logs")
        SessionLogs = sessionmaker(bind=engine_logs)

        with SessionLogs() as s:
            for t in tabelas:
                model = tabela_para_modelo[t]
                query = s.query(model)
                if usuario_filtro:
                    query = query.filter(model.usuario_id.like(f"%{usuario_filtro}%"))
                if desde_iso:
                    query = query.filter(model.timestamp >= desde_iso)
                linhas = query.order_by(model.id.desc()).limit(limite).all()
                resultado[t] = {
                    "total_retornado": len(linhas),
                    "linhas": [
                        {c.name: getattr(row, c.name) for c in model.__table__.columns}
                        for row in linhas
                    ],
                }
        return jsonify({
            "filtros": {"tipo": tipo or "todos", "usuario": usuario_filtro, "desde": desde_str, "limite": limite},
            "tabelas": resultado,
        })
    except Exception as e:
        logger.error("admin_logs FAILED: %s", e, exc_info=True)
        _log_erro("/admin/logs", e, usuario_id="admin")
        return jsonify({"erro": "Erro ao consultar logs."}), 500


if __name__ == "__main__":
    # Em produção (PaaS como Railway/Render): o Procfile roda gunicorn,
    # então este bloco SÓ executa em dev local. Em prod, debug NUNCA pode ser True
    # (vaza traceback + permite execução arbitrária via Werkzeug debugger).
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    port = int(os.getenv("PORT", "5000"))
    app.run(debug=debug, host="127.0.0.1", port=port)
