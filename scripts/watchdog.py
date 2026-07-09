"""
watchdog.py — Mantém o servidor Flask vivo.

Monitora http://127.0.0.1:5000/health. Se cair, reinicia.
Limite: 10 restarts consecutivos pra evitar loop infinito.
"""

import os
import sys
import time
import subprocess
import signal
from urllib.request import urlopen
from urllib.error import URLError

PORT = 5000
HEALTH_URL = f"http://127.0.0.1:{PORT}/health"
MAX_RESTARTS = 10
RESTART_WINDOW = 300  # janela de 5 min pra contar restarts
CHECK_INTERVAL = 5    # checa a cada 5s


def server_up() -> bool:
    try:
        with urlopen(HEALTH_URL, timeout=3) as r:
            return r.status == 200
    except (URLError, ConnectionError, OSError):
        return False


def start_server() -> subprocess.Popen:
    """Sobe o Flask como subprocess. Sem auto-reload (mais estável)."""
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env = os.environ.copy()
    env["FLASK_DEBUG"] = "0"
    print(f"[watchdog] cwd: {project_dir}", flush=True)
    proc = subprocess.Popen(
        [sys.executable, "-c",
         "import os; os.environ['FLASK_DEBUG']='0'; "
         "from app import app; "
         f"app.run(debug=False, host='127.0.0.1', port={PORT}, use_reloader=False)"],
        cwd=project_dir,
        env=env,
    )
    return proc


def main():
    print(f"[watchdog] Iniciando Flask no port {PORT}")
    proc = start_server()
    restarts = []
    last_check = 0

    try:
        while True:
            time.sleep(1)
            now = time.time()

            # Só checa a cada CHECK_INTERVAL
            if now - last_check < CHECK_INTERVAL:
                continue
            last_check = now

            if server_up():
                continue

            # Servidor caiu — tenta matar o processo antigo e reiniciar
            print(f"[watchdog] Servidor DOWN às {time.strftime('%H:%M:%S')}")

            try:
                proc.terminate()
                proc.wait(timeout=5)
            except (subprocess.TimeoutExpired, ProcessLookupError):
                try:
                    proc.kill()
                except ProcessLookupError:
                    pass

            # Limpa janela de restarts
            now2 = time.time()
            restarts = [t for t in restarts if now2 - t < RESTART_WINDOW]

            if len(restarts) >= MAX_RESTARTS:
                print(f"[watchdog] {MAX_RESTARTS} restarts em {RESTART_WINDOW}s — parando. "
                      "Provavelmente algo está errado. Verifique os logs do Flask.")
                sys.exit(1)

            print(f"[watchdog] Reiniciando... ({len(restarts) + 1}/{MAX_RESTARTS})")
            proc = start_server()
            restarts.append(now2)
            time.sleep(2)  # espera subir

    except KeyboardInterrupt:
        print("\n[watchdog] Encerrando...")
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass


if __name__ == "__main__":
    main()