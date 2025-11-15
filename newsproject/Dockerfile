FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

COPY . .

ENV PYTHONUNBUFFERED=1

RUN chmod +x build.sh && ./build.sh
EXPOSE 10000

CMD ["gunicorn", "newsproject.wsgi:application", "--config", "gunicorn_config.py"]



