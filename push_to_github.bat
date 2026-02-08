@echo off
echo ===================================================
echo   Setting up Git Repository for Taha Zaman
echo ===================================================

echo [1/6] Removing old git history...
rd /s /q .git

echo [2/6] Initializing new git repo...
git init

echo [3/6] Adding files...
git add .

echo [4/6] Committing files...
git commit -m "Initial commit by Taha Zaman: MLOps Pipeline"

echo [5/6] Adding remote origin...
git remote add origin https://github.com/TahaZaman6547/Water_Potability_Prediction.git

echo [6/6] Pushing to GitHub...
echo (You may be prompted to sign in)
git push -u origin main

echo ===================================================
echo   Done!
echo ===================================================
pause
