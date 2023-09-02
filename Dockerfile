FROM python:3.11-slim-bullseye

RUN pip install pipx
RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
copy meta_morph_pix meta_morph_pix

RUN poetry install

CMD ["poetry", "run", "python", "-m", "meta_morph_pix"]