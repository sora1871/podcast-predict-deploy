#!/bin/bash

# FastAPI をバックグラウンドで起動
uvicorn api.main:app --host 0.0.0.0 --port 8000 &

# Streamlit をフォアグラウンドで起動（ログも表示される）
streamlit run ui/main.py --server.port=8501 --server.address=0.0.0.0
