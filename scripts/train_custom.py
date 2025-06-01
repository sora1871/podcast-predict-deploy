# scripts/train_custom.py

import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.metrics import mean_squared_error

from scripts.basic_feature import create_train_data
from scripts.train_runner import run_baseline_training

def main():
    x_train, y_train, id_train = create_train_data("data/train.csv")

    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("PodcastPrediction")

    with mlflow.start_run(run_name="custom_training"):
        train_oof, imp, metrics = run_baseline_training(x_train, y_train, id_train)

        for i, (fold, rmse_tr, rmse_va) in enumerate(metrics):
            mlflow.log_metric(f"custom_rmse_train_fold{i}", rmse_tr)
            mlflow.log_metric(f"custom_rmse_val_fold{i}", rmse_va)

        oof_rmse = np.sqrt(mean_squared_error(y_train, train_oof["pred"]))
        mlflow.log_metric("custom_oof_rmse", oof_rmse)

if __name__ == "__main__":
    main()
