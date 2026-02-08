# MLOps Capstone Project: Water Potability Prediction
## Final Classification Pipeline Report

**Author:** Taha Zaman
**Date:** February 2026
**Repository:** [https://github.com/TahaZaman6547/Water_Potability_Prediction](https://github.com/TahaZaman6547/Water_Potability_Prediction)

---

## 1. Executive Summary
This project implements an end-to-end Machine Learning Operations (MLOps) pipeline for predicting water potability. The system automates the lifecycle from data ingestion to deployment, ensuring reproducibility, scalability, and robust experiment tracking. The final product is a containerized application consisting of a FastAPI inference engine and a Streamlit user interface, orchestrated via Docker Compose.

---

## 2. Pipeline Architecture & Diagram

The pipeline is structured to handle data flow automatically while maintaining version control at every stage.

```mermaid
graph TD
    subgraph DataOps [Data Operations]
        A[Ingest Data (GitHub)] -->|Raw CSV| B(Data Preprocessing)
        B -->|Feature Engineering| C(Split Train/Test)
        C -->|Versioned Data| D{DVC Storage}
    end

    subgraph MLOps [Model Operations]
        D -->|Load Data| E[Train Random Forest]
        E -->|Hyperparameters| F[W&B Experiment Tracking]
        E -->|Metrics: F1, Accuracy| F
        E -->|Serialize Model| G[Model Registry (W&B Artifacts)]
    end

    subgraph DevOps [Deployment Operations]
        G -->|Download Artifact| H[FastAPI Backend]
        H -->|REST API| I[Streamlit Frontend]
        I -->|User Interface| J[End User]
    end
```

---

## 3. Design Decisions & Justification

### **3.1 Technical Stack Selection**
| Component | Tool Selected | Justification |
| :--- | :--- | :--- |
| **Data Versioning** | **DVC** | Selected for its ability to handle large files and dataset versioning alongside Git without bloating the repository size. It ensures that every model training run is linked to a specific version of the data. |
| **Experiment Tracking** | **Weights & Biases (W&B)** | Chosen over MLflow for its superior visualization capabilities and cloud-hosted dashboard, which simplifies collaboration and remote monitoring without managing a tracking server. |
| **Model** | **Random Forest** | Analyzing the tabular nature of the dataset, Random Forest provides robust baseline performance with minimal overfitting risks compared to Neural Networks. It is also CPU-efficient, meeting resource constraints. |
| **Backend** | **FastAPI** | Selected for its high performance (Starlette-based) and automatic validation via Pydantic. The auto-generated Swagger UI simplifies API testing. |
| **Frontend** | **Streamlit** | Chosen to enable rapid prototyping of the user interface directly in Python, reducing development time compared to React/Angular. |

### **3.2 Pipeline Configuration**
The pipeline is configured as a **Directed Acyclic Graph (DAG)** via `dvc.yaml`. This configuration was chosen because:
1.  **Dependency Management:** It automatically detects which stages need re-running based on file changes (e.g., if `data_preprocessing.py` changes, DVC knows to re-run only preprocessing and training, not data collection).
2.  **Isolation:** Each stage runs in its own process, preventing global state pollution.
3.  **Portability:** The entire training workflow can be reproduced on any machine with a single command (`dvc repro`).

---

## 4. Trade-offs & Analysis

### **Reproducibility vs. Development Speed**
*   **Trade-off:** Implementing strict versioning with DVC and Docker increases initial setup time compared to running ad-hoc notebooks.
*   **Reflection:** This complexity pays off by eliminating "it works on my machine" issues. Any developer can clone the repo and reproduce the exact model state.

### **Scalability vs. Complexity**
*   **Trade-off:** The current architecture uses a synchronous REST API (FastAPI) which may bottleneck under massive concurrent loads compared to asynchronous message queues (Kafka/RabbitMQ).
*   **Reflection:** For the scoped requirements, this architecture is sufficient and keeps infrastructure costs low. Scaling can be achieved horizontally by deploying closer replica containers on Kubernetes/Cloud Run.

### **Ease of Use vs. Security**
*   **Trade-off:** We prioritized ease of use by including `run_locally.bat` scripts and simple Docker commands.
*   **Reflection:** In a production environment, stricter security measures (secrets management for API keys, HTTPS) would ideally be enforced over simple environment variable files.

### **Resource Constraints**
*   **Constraint:** The project needed to be lightweight enough to run on standard local machines.
*   **Solution:** By using standard machine learning libraries (Scikit-Learn) instead of heavy Deep Learning frameworks (TensorFlow/PyTorch), the docker images remain relatively small (<1GB), and the model trains in seconds on a standard CPU.

---

## 5. Deployment Instructions

### **Local Execution**
1.  **Clone:** `git clone https://github.com/TahaZaman6547/Water_Potability_Prediction.git`
2.  **Run:** Execute `start_app.bat` (Windows) or `docker-compose up` (Universal).
3.  **Access:**
    *   **Frontend:** http://localhost:8501
    *   **API:** http://localhost:8000/docs

---
*End of Report*
