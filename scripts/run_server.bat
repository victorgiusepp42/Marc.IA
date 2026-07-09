@echo off
REM run_server.bat — Sobe o Flask e reinicia se cair.
REM Uso: run_server.bat

setlocal
cd /d "%~dp0\.."

:loop
echo [%date% %time%] Iniciando Marc.IA Flask...
python -c "import os; os.environ['FLASK_DEBUG']='0'; from app import app; app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)"
echo [%date% %time%] Flask caiu. Reiniciando em 3s...
timeout /t 3 /nobreak >nul
goto loop