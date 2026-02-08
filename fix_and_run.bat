@echo off
echo ===================================================
echo   Fixing and Launching Water Potability App
echo ===================================================

echo [1/5] Killing any lingering Python processes...
taskkill /F /IM python.exe /T 2>nul

echo [2/5] removing DVC lock files...
if exist ".dvc\tmp\rwlock" del ".dvc\tmp\rwlock"
if exist ".dvc\cache" rd /s /q ".dvc\cache"

echo [3/5] Running DVC Pipeline (This might take a minute)...
dvc repro

echo [4/5] Starting Backend...
start "Backend API" cmd /k "cd src/backend && uvicorn app:app --host 0.0.0.0 --port 8000 --reload"

echo [5/5] Waiting for backend to initialize (5s)...
timeout /t 5

echo [6/6] Starting Frontend...
cd src/frontend
streamlit run Water_Prediction.py
pause
