@echo off
echo ===================================================
echo   Starting Water Potability Prediction App
echo ===================================================

echo [1/3] Ensuring backend is running...
start "MLOps Backend" cmd /k "cd src/backend && uvicorn app:app --host 0.0.0.0 --port 8000 --reload"

echo [2/3] Waiting for backend to initialize (5s)...
timeout /t 5

echo [3/3] Starting Frontend...
cd src/frontend
streamlit run Water_Prediction.py

pause
