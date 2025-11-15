FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

RUN python -W ignore::RuntimeWarning manage.py collectstatic --noinput || true
COPY build.sh /build.sh
RUN chmod +x /build.sh

ENTRYPOINT ["/build.sh"]
EXPOSE 10000

CMD ["gunicorn", "newsproject.wsgi:application", "--config", "gunicorn_config.py"]



