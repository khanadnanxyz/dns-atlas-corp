FROM python:3.7-alpine

RUN apk add --no-cache --virtual .pynacl_deps build-base openssl-dev libffi-dev

COPY . /app
WORKDIR /app

RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

RUN chmod +x ./devops/run.sh

EXPOSE 5000
ENTRYPOINT ["./devops/run.sh"]
