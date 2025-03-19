FROM python:3.12.9-slim-bookworm AS python-base

ENV POETRY_VERSION=2.1.1 \
    POETRY_HOME=/opt/poetry \
    PATH="/opt/poetry/bin:$PATH" \
    POETRY_CACHE_DIR=/opt/.cache

RUN apt-get update && apt-get install -y curl net-tools && \
    python3 -m venv $POETRY_HOME && \
    $POETRY_HOME/bin/pip install --upgrade pip && \
    $POETRY_HOME/bin/pip install poetry==$POETRY_VERSION && \
    poetry --version && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# ----------------- Dev Stage -----------------
FROM python-base AS dev

WORKDIR /app

COPY --from=python-base $POETRY_HOME $POETRY_HOME
ENV PATH="${POETRY_HOME}/bin:$PATH"

COPY poetry.lock pyproject.toml ./

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN poetry install --no-interaction --no-cache --no-root --with dev


EXPOSE 8000

CMD ["/app/.venv/bin/fastapi", "dev", "src/deep_trace/api.py"]


# ----------------- Prd Stage -----------------
FROM python-base AS deep-trace

WORKDIR /app

COPY --from=python-base $POETRY_HOME $POETRY_HOME

ENV PATH="${POETRY_HOME}/bin:$PATH"

COPY poetry.lock pyproject.toml ./

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
RUN poetry install --no-interaction --no-cache --no-root --without dev

COPY . /app

EXPOSE 80
CMD ["/app/.venv/bin/uvicorn", "src.deep_trace.api:app", "--host", "0.0.0.0", "--port", "80"]
