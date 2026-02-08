import pandas as pd
import numpy as np
import pickle
import json
import os
import wandb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_data(file_path):
    return pd.read_csv(file_path)

def main():
    try:
        # Initialize W&B
        wandb.init(project="water-potability-prediction", job_type="evaluate")

        # Load data
        test_path = os.path.join('data', 'preprocessing', 'test_processed.csv')
        if not os.path.exists(test_path):
             raise FileNotFoundError(f"{test_path} not found.")
        
        test_df = pd.read_csv(test_path)
        
        target_col = 'Potability'
        X_test = test_df.drop(columns=[target_col])
        y_test = test_df[target_col]

        # Load model with artifact handling
        # For now, load local model, but in a real pipeline we might download from registry.
        # But this script runs locally after training stage in DVC.
        model_path = os.path.join('models', 'rf_model.pkl')
        if not os.path.exists(model_path):
             raise FileNotFoundError(f"{model_path} not found.")
        
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        # Predict
        print("Evaluating model...")
        y_pred = model.predict(X_test)

        # Metrics
        acc = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        metrics = {
            "test_accuracy": acc,
            "test_precision": precision,
            "test_recall": recall,
            "test_f1": f1
        }
        
        print(f"Metrics: {metrics}")
        wandb.log(metrics)

        # Save metrics
        reports_dir = 'reports'
        os.makedirs(reports_dir, exist_ok=True)
        metrics_path = os.path.join(reports_dir, 'eval_metrics.json')
        
        with open(metrics_path, 'w') as f:
            json.dump(metrics, f, indent=4)
            
        print("Evaluation completed.")
        wandb.finish()

    except Exception as e:
        print(f"Error in evaluation: {e}")
        raise

if __name__ == '__main__':
    main()
