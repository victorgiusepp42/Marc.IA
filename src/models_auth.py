"""
Model SQLAlchemy para usuários autenticados via Google OAuth.

Sprint 3 — implementado em 2026-07-05 conforme plano sequential-coalescing-castle.md.
Vincula Sessao (que continua usando email como chave string) a uma identidade real.
"""

from datetime import datetime, timezone

from flask_login import UserMixin

from src.database import db


class Usuario(db.Model, UserMixin):
    """Usuário autenticado via Google OAuth.

    Identidade primária é o `google_id` (campo `sub` do id_token do Google).
    Email é indexado pra busca rápida e é o que usamos como `usuario_id` no
    resto do app (mantém compatibilidade com Sessao.carregar_ou_criar).
    """

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(128), unique=True, nullable=False, index=True)
    email = db.Column(db.String(256), unique=True, nullable=False, index=True)
    nome = db.Column(db.String(256), nullable=True)
    foto_url = db.Column(db.String(512), nullable=True)
    criado_em = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    ultimo_acesso = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # --- Flask-Login interface ---
    # UserMixin já dá is_authenticated, is_active, is_anonymous, get_id().
    # get_id() retorna str(self.id) por padrão — usamos o PK inteiro.
    # NÃO confundir com `google_id` (que é o sub do Google).

    def __repr__(self) -> str:
        return f"<Usuario {self.email}>"