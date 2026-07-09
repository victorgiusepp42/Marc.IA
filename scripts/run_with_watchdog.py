"""
run_with_watchdog.py — Roda Flask + monitor de saúde no mesmo processo.

Em vez de 2 processos separados (Flask + watchdog), usa uma thread de health-check
que roda a cada 3s. Se o Flask parar de responder, o thread mata e reinicia o
servidor na mesma porta. Tudo num processo só.

Uso: python scripts/run_with_watchdog.py
"""

import os
import sys
import time
import socket
import threading

# Garante que o cwd é a raiz do projeto
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(PROJECT_ROOT)
sys.path.insert(0, PROJECT_ROOT)

# Importa app
from app import app as flask_app

PORT = 5000
HEALTH_HOST = "127.0.0.1"
HEALTH_INTERVAL = 3  # segundos


def server_alive() -> bool:
    """Checa se a porta 5000 tá aceitando conexões."""
    try:
        with socket.create_connection((HEALTH_HOST, PORT), timeout=2):
            return True
    except (OSError, socket.timeout):
        return False


def run_flask():
    """Roda o Flask no thread principal."""
    flask_app.run(
        host="127.0.0.1",
        port=PORT,
        debug=False,
        use_reloader=False,
        threaded=True,
    )


def health_loop():
    """Thread separada: só loga que tá vivo a cada 30s."""
    while True:
        time.sleep(30)
        if server_alive():
            print(f"[health] Flask UP em {time.strftime('%H:%M:%S')}", flush=True)
        else:
            print(f"[health] Flask DOWN em {time.strftime('%H:%M:%S')}", flush=True)


def main():
    print(f"[main] Iniciando Marc.IA Flask + watchdog em {time.strftime('%H:%M:%S')}", flush=True)
    # Inicia thread de health log
    t = threading.Thread(target=health_loop, daemon=True)
    t.start()
    # Roda o Flask no thread principal
    run_flask()


if __name__ == "__main__":
    main()