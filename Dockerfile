FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHON UNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libsqlite3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# remove for render
EXPOSE 8000

# replace port 8000 by $PORT for render
CMD ["sh", "-c", \
    "python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]