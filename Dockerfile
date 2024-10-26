FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=UserDataEnricher.settings

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000
