FROM python:3.10-alpine3.18

COPY . /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev openssl-dev curl rust cargo

RUN pip install poetry

RUN poetry install