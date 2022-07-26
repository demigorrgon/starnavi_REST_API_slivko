FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /social-app
WORKDIR /social-app

COPY . /social-app/
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev 
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

# CMD [ "gunicorn",  "--bind", ":8000", "--workers", "4", "social_network_core.wsgi:application"]