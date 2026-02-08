@echo off
echo ===================================================
echo   Starting Water Potability App (Robust Launch)
echo ===================================================

:: Get the directory where this script is located
set "PROJECT_ROOT=%~dp0"
cd /d "%PROJECT_ROOT%"

echo [1/3] Starting Backend API...
:: Start backend in a new window, but keep window open if it fails (cmd /k)
start "Backend API" cmd /k "cd src/backend && uvicorn app:app --host 0.0.0.0 --port 8000 --reload"

echo [2/3] Waiting for API to initialize (5 seconds)...
timeout /t 5

echo [3/3] Starting Frontend UI...
:: Run streamlit in the current window so we can see errors
cd src/frontend
streamlit run Water_Prediction.py

:: If streamlit crashes, pause so user can see error
if %errorlevel% neq 0 (
    echo [ERROR] Streamlit crashed!
    pause
)
