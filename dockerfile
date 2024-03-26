FROM python:3.10-alpine3.18

COPY . /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev openssl-dev curl rust cargo

RUN pip install poetry pytest

RUN poetry install

RUN echo "export PYNGUIN_DANGER_AWARE=1" >> ~/.bashrc

CMD ["poetry", "run", "python", "main.py"]
