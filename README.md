# Simple Python Flask App in Docker

This project contains a simple Python Flask application running inside a Docker container.

## Description

- Flask application that responds to HTTP requests and returns the message "Hello, World!".
- The image is based on `python:3.9-slim`.
- The application is run using Docker Compose.
- Port 5000 is exposed for external access.

## Requirements

- Docker and Docker Compose installed.
- `make` command available.

## Usage

- Create image:
bash -> make build

- Start image:
bash -> make run

- Clean and stop image:
bash -> make clean

After starting the container, the application will be available at:
http://localhost:5000

License
MIT
