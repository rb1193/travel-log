FROM python:3.8.3-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y postgresql gcc python3-dev musl-dev libpq-dev

# install dependencies
RUN pip3.8 install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3.8 install -r requirements.txt --no-cache