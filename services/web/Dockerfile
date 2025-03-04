# services/web/Dockerfile

FROM python:3.12-slim-bullseye

WORKDIR /usr/src/web

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHOBUNBUFFERED 1
ENV PYTHONPATH=/usr/src

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY app app/

WORKDIR ./app