# 🚰 Water Potability Prediction (MLOps Capstone)

An End-to-End MLOps pipeline for predicting water potability using machine learning. This project demonstrates reproducibility, automation, experiment tracking, and deployment using modern MLOps tools.

---

## 🚀 Project Overview

This repository contains a complete MLOps pipeline designed to predict whether water is safe for consumption based on its chemical properties.

**Key Features:**
- **Reproducible Pipeline:** Managed by DVC (Data Version Control).
- **Experiment Tracking:** Weights & Biases (W&B) integration for metrics and artifacts.
- **Model Registry:** Automated model versioning with W&B.
- **CI/CD:** GitHub Actions for automated training and Docker builds.
- **Deployment:** Containerized FastAPI backend and Streamlit frontend.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **ML Framework:** Scikit-Learn (Random Forest)
- **Data Versioning:** DVC
- **Experiment Tracking:** Weights & Biases
- **API:** FastAPI
- **Frontend:** Streamlit
- **Containerization:** Docker & Docker Compose
- **Orchestration:** GitHub Actions

---

## 📂 Project Structure

```bash
├── .github/workflows   # CI/CD Workflows
├── data                # Data directory (managed by DVC)
├── models              # Trained models
├── reports             # Evaluation metrics and figures
├── src
│   ├── backend         # FastAPI application source
│   ├── data            # Data collection & preprocessing scripts
│   ├── deploy          # Deployment configurations
│   ├── frontend        # Streamlit application source
│   ├── models          # Model training & evaluation scripts
│   └── visualization   # Visualization scripts
├── dvc.yaml            # DVC Pipeline definition
├── params.yaml         # Training parameters
├── requirements.txt    # Project dependencies
└── Makefile            # Command shortcuts
```

---

## ⚡ Quick Start

### 1. Prerequisites
- Python 3.11+
- Docker & Docker Compose
- [Weights & Biases Account](https://wandb.ai) (API Key required)

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/TahaZaman6547/Water_Potability_Prediction.git
cd Water_Potability_Prediction
pip install -r requirements.txt
```

### 3. Setup W&B

Login to Weights & Biases:

```bash
wandb login
# Paste your API key when prompted
```

### 4. Run the Pipeline

Execute the entire data-to-model pipeline using DVC:

```bash
dvc repro
```
*This command will:*
1. Download the dataset.
2. Preprocess the data.
3. Train the Random Forest model.
4. Evaluate the model and save metrics.
5. Log everything to W&B.

---

## 🐳 Deployment

You can run the application locally using Docker Compose.

1. Navigate to the deploy directory:
   ```bash
   cd src/deploy
   ```

2. Start the services:
   ```bash
   # Linux/Mac
   export WANDB_API_KEY=your_api_key_here
   docker-compose up --build

   # Windows (PowerShell)
   $env:WANDB_API_KEY="your_api_key_here"
   docker compose up --build
   ```

3. Access the App:
   - **Frontend (Streamlit):** [http://localhost:8501](http://localhost:8501)
   - **Backend API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📊 Pipeline Design

The pipeline follows a modular structure:

1. **Data Ingestion:** Downloads raw data from a remote source.
2. **Preprocessing:** Handles missing values and feature engineering.
3. **Training:** Trains a Random Forest Classifier and logs artifacts to W&B.
4. **Evaluation:** Computes accuracy, precision, recall, and F1-score.
5. **Deployment:** Serves the best model via REST API.

![Pipeline Diagram](pipeline_design.md)

---

## 📝 Deliverables Checklist

- [x] **GitHub Repository:** Code, Dockerfiles, and CI/CD workflows complete.
- [x] **Deployed App:** Dockerized setup ready for cloud deployment.
- [x] **Experiment Tracking:** Verified W&B integration.
- [x] **Design Diagram:** Included in `pipeline_design.md`.
- [x] **Final Report:** Included in `final_report.md`.

---

## ⚖️ Trade-offs & Design Decisions

See [Final Report](final_report.md) for a detailed breakdown of design choices, including why Random Forest was chosen over Deep Learning and the benefits of using FastAPI + Streamlit.

---

**Author:** Taha Zaman
**Course:** MLOps Capstone
