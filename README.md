# DevOps Sample API

This project demonstrates Dockerization, environment-based configuration,
health checks, logging, and CI using GitHub Actions.

## Features
- Simple Flask API
- Dockerized application
- Environment variable based configuration
- Health check endpoint
- Request logging
- Docker Compose support
- CI pipeline using GitHub Actions

---

## API Endpoints

### GET /
Returns a simple message to confirm the API is running.

### POST /echo
Echoes back the JSON payload sent in the request.

### GET /health
Health check endpoint used by Docker.

Response:
```json
{ "status": "ok" }
