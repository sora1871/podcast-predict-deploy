import joblib
import pandas as pd
from pathlib import Path

from scripts.basic_feature import preprocess_features
from scripts.feature_isna import handle_missing_values

# モデルの読み込み（5fold）
models = []
model_dir = Path(__file__).resolve().parent.parent / "models"

for i in range(5):
    model_path = model_dir / f"model_lgb_fold{i}.joblib"
    models.append(joblib.load(model_path))

# モデルが期待する列
EXPECTED_COLUMNS = [
    "Podcast_Name",
    "Episode_Title",
    "Episode_Length_minutes",
    "Genre",
    "Host_Popularity_percentage",
    "Publication_Day",
    "Publication_Time",
    "Guest_Popularity_percentage",
    "Number_of_Ads",
    "Episode_Sentiment",
    "Episode_Length_minutes_raw",
    "Episode_Length_minutes_was_missing",
    "Guest_Popularity_percentage_raw",
    "Guest_Popularity_percetage_was_missing"
]

# 前処理
def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = preprocess_features(df)
    df = handle_missing_values(df)
    df = df[EXPECTED_COLUMNS]
    return df

# 予測関数（5モデル平均）
def predict_single(input_dict: dict) -> float:
    df = pd.DataFrame([input_dict])
    df = preprocess(df)
    preds = [model.predict(df)[0] for model in models]
    return float(sum(preds) / len(preds))
