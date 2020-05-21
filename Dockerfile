FROM python:3

ADD * /usr/src/myapp/

WORKDIR /usr/src/myapp

RUN pip install -r "requirements.txt"
