#  Predict Podcast Listening Time - Dockerized ML Web App

このプロジェクトは、ポッドキャストのメタデータ（ジャンル・出演者の人気度・広告数など）をもとに、  
ユーザーのリスニング時間（何分聞かれるか）を予測する機械学習アプリケーションです。

LightGBM による予測モデルを FastAPI 経由で提供し、Streamlit による入力UIで可視化。  
さらに Docker 化により、誰でもすぐにローカルで再現可能です。

---
まだ、デプロイができてないので、完成したら追記します。

---

##  使用した特徴量（全14項目）

| 特徴量名 | 説明 |
|----------|------|
| `Podcast_Name` | 番組名（カテゴリ） |
| `Episode_Title` | エピソードのタイトル |
| `Episode_Length_minutes` | エピソードの長さ（分） |
| `Genre` | ジャンル（カテゴリ） |
| `Host_Popularity_percentage` | ホストの人気度（%） |
| `Publication_Day` | 公開された曜日 |
| `Publication_Time` | 公開された時間（HH:MM） |
| `Guest_Popularity_percentage` | ゲストの人気度（%） |
| `Number_of_Ads` | 広告の数 |
| `Episode_Sentiment` | 内容のトーン（例: Positive） |
| `Episode_Length_minutes_raw` | 補完前の長さデータ |
| `Episode_Length_minutes_was_missing` | 長さの欠損フラグ |
| `Guest_Popularity_percentage_raw` | ゲスト人気度の生データ |
| `Guest_Popularity_percetage_was_missing` | ゲスト人気度の欠損フラグ |

---

##  主な機能

- ユーザーが指定した条件からリスニング時間を予測
- LightGBM（5-Fold）での平均予測を使用
- 入力特徴量に対する感度分析（Streamlit上でグラフ表示）
- FastAPIによるAPIサーバー実装済み（Swagger UI対応）
- Dockerで一発起動できる環境を提供

---

##  Dockerでの実行方法（推奨）

```bash
# イメージをビルド
docker build -t podcast-app .

# コンテナを起動
docker run -p 8000:8000 -p 8501:8501 podcast-app
Streamlit UI: http://localhost:8501

FastAPI Swagger UI: http://localhost:8000/docs

 API エンドポイント（FastAPI）
/predict (POST)
 入力（JSON）

{
  "Episode_Length_minutes": 45,
  "Genre": "Technology",
  "Host_Popularity_percentage": 80,
  ...
}
 出力（例）

{
  "predicted_time": 38.2
}
 Swagger UIでインタラクティブに試せます → http://localhost:8000/docs

 ディレクトリ構成

podcast-predict-deploy/
├── api/               # FastAPI アプリ
│   ├── main.py
│   └── predict.py
├── ui/                # Streamlit アプリ
│   └── main.py
├── scripts/           # 前処理・共通ロジック
│   ├── basic_feature.py
│   └── feature_isna.py
├── models/            # LightGBM モデルファイル
│   └── model_lgb_fold{0-4}.joblib
├── Dockerfile         # Docker ビルド用
├── entrypoint.sh      # FastAPI + Streamlit 起動スクリプト
├── requirements.txt   # 依存ライブラリ
└── README.md
 補足（開発背景）
このプロジェクトは「実務を想定した構成」で設計しており、

Webアプリ化（Streamlit）

API提供（FastAPI）

再現性と移植性（Docker化）
を重視しました。
