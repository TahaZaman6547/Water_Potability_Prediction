@echo off
echo ===================================================
echo   EMERGENCY FIX & RUN SCRIPT
echo ===================================================

echo [1/5] Installing Dependencies (Just to be safe)...
pip install -r requirements.txt >nul 2>&1

echo [2/5] Running Data Collection...
python src/data/data_collection.py
if %errorlevel% neq 0 (
    echo [ERROR] Data Collection Failed!
    pause
    exit /b %errorlevel%
)

echo [3/5] Running Data Preprocessing...
python src/data/data_preprocessing.py
if %errorlevel% neq 0 (
    echo [ERROR] Data Preprocessing Failed!
    pause
    exit /b %errorlevel%
)

echo [4/5] Running Model Training (This creates the missing model file)...
python src/models/model_building.py
if %errorlevel% neq 0 (
    echo [ERROR] Model Training Failed!
    pause
    exit /b %errorlevel%
)

echo [5/5] Launching App...
start "Backend API" cmd /k "cd src/backend && uvicorn app:app --host 0.0.0.0 --port 8000 --reload"
timeout /t 5
cd src/frontend
streamlit run Water_Prediction.py

pause
