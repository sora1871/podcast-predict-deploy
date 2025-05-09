# Dockerfile
FROM python:3.10

# 作業ディレクトリ作成
WORKDIR /app

# プロジェクトファイルをすべてコピー
COPY . .

# 依存パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# 実行権限を付けてエントリースクリプト起動
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
