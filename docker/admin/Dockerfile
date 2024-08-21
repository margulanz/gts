FROM python:3.11.5-alpine

RUN apk update && apk add python3-dev gcc libc-dev

ENV PYTHONUNBUFFERED 1

WORKDIR /app_admin

RUN pip install --upgrade pip
ADD ./requirements.txt /app_admin/
RUN pip install -r requirements.txt

ADD ./news /app_admin/
ADD ./docker/admin /app_admin/docker/