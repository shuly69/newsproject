FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

RUN python -W ignore::RuntimeWarning manage.py collectstatic --noinput || true
RUN python manage.py migrate 
EXPOSE 10000

CMD ["gunicorn", "newsproject.wsgi:application", "--config", "gunicorn_config.py"]



