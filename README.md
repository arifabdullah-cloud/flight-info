# Flight Info

Real-time flight monitoring and operational analytics platform.

## Goals

This project exists for hands-on learning around:

- FastAPI
- Data ingestion
- Background jobs
- PostgreSQL
- Docker
- Cloud deployment
- Observability
- Operational engineering

## Initial Scope

- Pull live flight data from OpenSky API
- Store aircraft snapshots
- Expose REST API endpoints
- Build operational dashboards
- Add anomaly detection and alerting later

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Docker Compose

## Current Features

- Live OpenSky flight ingestion
- Malaysia/SEA regional filtering
- Flight statistics endpoint
- Structured flight parsing
- FastAPI REST API

## Current Endpoints

### Health
GET /health

### Live Flights
GET /flights/live

### Flight Statistics
GET /stats

## Roadmap

See:
- docs/roadmap/roadmap.md

## Documentation

- Architecture decisions:
  - docs/decisions/

- Learning journal:
  - docs/learning-journal/
