FROM python:3.11-alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Системные зависимости для psycopg2 и других пакетов
RUN apk add --no-cache \
    build-base \
    postgresql-client \
    postgresql-dev \
    musl-dev \
    libffi-dev \
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev

# Python зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Код проекта
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]










# FROM python:3.11-alpine3.16

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# COPY requirements.txt /app/requirements.txt
# COPY . /app

# RUN apk add --no-cache postgresql-client build-base postgresql-dev && \
#     pip3 install -r requirements.txt

# COPY . . 

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]