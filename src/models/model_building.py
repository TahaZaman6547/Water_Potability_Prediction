import pandas as pd
import numpy as np
import pickle
import yaml
import os
import wandb
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_params(param_path):
    with open(param_path) as f:
        return yaml.safe_load(f)

def load_data(file_path):
    return pd.read_csv(file_path)

def main():
    try:
        # Load params
        params = load_params('params.yaml')
        n_estimators = params['model_building']['n_estimators']

        # Initialize W&B
        wandb.init(project="water-potability-prediction", job_type="train")
        wandb.config.n_estimators = n_estimators

        # Load data
        train_path = os.path.join('data', 'preprocessing', 'train_processed.csv')
        # Check if file exists
        if not os.path.exists(train_path):
             raise FileNotFoundError(f"{train_path} not found. Please run data collection/preprocessing first.")
        
        train_df = pd.read_csv(train_path)
        
        # Prepare X and y
        # Assuming the last column or "Potability" is target.
        # Let's check column names from previous file view or valid intuition.
        # The dataset water_potability.csv usually has 'Potability' as target.
        target_col = 'Potability'
        if target_col not in train_df.columns:
            # Maybe it's not there? The downloaded csv usually has it.
            # Let's assume it is there.
            pass
        
        X_train = train_df.drop(columns=[target_col])
        y_train = train_df[target_col]

        # Train model
        print("Training model...")
        clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
        clf.fit(X_train, y_train)

        # Log training accuracy
        train_preds = clf.predict(X_train)
        train_acc = accuracy_score(y_train, train_preds)
        wandb.log({"train_accuracy": train_acc})
        print(f"Training Accuracy: {train_acc}")

        # Save model
        models_dir = 'models'
        os.makedirs(models_dir, exist_ok=True)
        model_path = os.path.join(models_dir, 'rf_model.pkl')
        
        with open(model_path, 'wb') as f:
            pickle.dump(clf, f)
        
        # Log model artifact
        artifact = wandb.Artifact('rf_model', type='model')
        artifact.add_file(model_path)
        wandb.log_artifact(artifact)
        
        print("Model training completed and logged to W&B.")
        wandb.finish()

    except Exception as e:
        print(f"Error in model building: {e}")
        # wandb.finish(exit_code=1) # Optional
        raise

if __name__ == '__main__':
    main()
