FROM python:3.12-alpine3.20
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache \
    jpeg-dev \
    zlib-dev \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev \
    postgresql-dev 

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

USER django-user