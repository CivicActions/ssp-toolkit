FROM python:3.10-slim AS python-base

RUN apt update && apt install -y --no-install-recommends \
    gcc \
    g++ \
    libffi-dev \
    musl-dev \
    build-essential \
    && apt clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=2.0.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

RUN pip install "poetry==$POETRY_VERSION"

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

COPY . ./

RUN poetry config virtualenvs.create false

RUN poetry install

CMD ["python", "tools/watcher.py"]
