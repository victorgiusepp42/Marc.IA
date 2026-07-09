"""
Configuração central do SQLAlchemy.
Instância única do db — importada por models e app.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
