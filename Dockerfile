FROM python:3.7-alpine

RUN apk add --no-cache --virtual .pynacl_deps build-base openssl-dev libffi-dev

ADD . /app
WORKDIR /app

RUN apk update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python","app.py"]