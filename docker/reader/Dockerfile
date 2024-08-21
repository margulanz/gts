FROM python:3.11.5-alpine

RUN apk update && apk add python3-dev gcc libc-dev

ENV PYTHONUNBUFFERED 1

WORKDIR /app_reader

RUN pip install --upgrade pip
ADD ./requirements.txt /app_reader/
RUN pip install -r requirements.txt

ADD ./news_reader /app_reader/
ADD ./docker/reader /app_reader/docker/