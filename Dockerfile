FROM python:3.12-slim

# /app ディレクトリを作成して移動
WORKDIR /app

RUN apt-get update && apt-get install -y default-jre && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt