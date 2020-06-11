FROM python:3.7-alpine

RUN apk add --no-cache --virtual .pynacl_deps build-base openssl-dev libffi-dev

WORKDIR /app

RUN apk update
RUN pip install --upgrade pip

ADD ./requirements.txt ./
RUN pip install -r requirements.txt

ADD ./web ./web
ADD ./dev_run.sh ./


RUN chmod +x dev_run.sh

EXPOSE 5000
ENTRYPOINT ["./dev_run.sh"]