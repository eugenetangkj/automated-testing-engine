FROM python:3.10-alpine3.18

COPY . /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev openssl-dev curl rust cargo

RUN pip install poetry pytest coverage pytest-cov pylint

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

ENV PYNGUIN_DANGER_AWARE=1

CMD ["poetry", "run", "python", "main.py"]
