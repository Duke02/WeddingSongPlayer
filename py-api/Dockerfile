# Install uv
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

ADD pyproject.toml .
ADD uv.lock .

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

FROM builder AS runtime

# Copy the project into the image
ADD . /app

EXPOSE 8000

CMD ["uvicorn", "wedding_song_player.main:app", "--host", "0.0.0.0", "--port", "8000"]
