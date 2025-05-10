# ベースイメージ：Python公式の軽量バージョン
FROM python:3.10-slim

# 作業ディレクトリの作成
WORKDIR /app

# 依存ファイルをコピー＆インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコードをすべてコピー
COPY . .

# エントリポイントスクリプトに実行権限を付与
RUN chmod +x entrypoint.sh

# 外部に公開するポート（Streamlit用）
EXPOSE 8501

# アプリの起動コマンド（FastAPI + Streamlit）
CMD ["./entrypoint.sh"]
