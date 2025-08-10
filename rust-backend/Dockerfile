# Shout out to the official documentation for this code - https://hub.docker.com/_/rust/#start-a-rust-instance-running-your-app

FROM rust:1.85 AS builder
WORKDIR /usr/src/app
COPY . .
RUN cargo install --path . --root /app

FROM debian:bullseye-slim AS runner
# RUN apt-get update && apt-get install -y extra-runtime-dependencies && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/bin/wedding-song-player /usr/local/bin/wedding-song-player

EXPOSE 8001

CMD ["app"]
