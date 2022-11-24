FROM python:3.11.0-alpine3.16

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add gcc python3-dev g++ make
RUN pip install flask Navec gunicorn

COPY . /usr/src/app/

CMD gunicorn --bind 0.0.0.0:8736 main:app
