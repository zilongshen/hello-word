FROM python:3.10-slim

WORKDIR /app

RUN pip install chromadb

EXPOSE 8000

CMD ["chroma", "run", "--host", "0.0.0.0", "--path", "/chroma/data"]