"""
Remove logs antigos de data/logs.db para manter DB saudável.
Política: manter últimos N dias (default 90).

Uso: python scripts/limpar_logs.py [--dias 90]

Documentado em data/kb_ip/00_meta/LOGGING.md.
"""
import argparse
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Garante que src/ é importável
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from flask import Flask
from src.database import db
from src.models import LogExecucao, LogErro


def main():
    parser = argparse.ArgumentParser(description="Limpa logs antigos do Marc.IA")
    parser.add_argument(
        "--dias", type=int, default=90,
        help="Manter logs dos últimos N dias (default: 90)",
    )
    args = parser.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.dias)

    app = Flask(__name__)
    data_dir = ROOT / "data"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{data_dir}/marcia.db"
    app.config["SQLALCHEMY_BINDS"] = {"logs": f"sqlite:///{data_dir}/logs.db"}
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        n_exec = LogExecucao.query.filter(LogExecucao.timestamp < cutoff).delete()
        n_err = LogErro.query.filter(LogErro.timestamp < cutoff).delete()
        db.session.commit()
        print(f"Removidos: {n_exec} execucoes, {n_err} erros (anteriores a {cutoff.date()})")
        print(f"Restantes: execucoes={LogExecucao.query.count()}, erros={LogErro.query.count()}")


if __name__ == "__main__":
    main()