# Architecture Decision Record

## Decision
Use FastAPI + PostgreSQL + React + Docker for the local reference implementation.

## Why
- Python supports test automation and simulator development.
- FastAPI provides typed REST/OpenAPI interfaces.
- PostgreSQL demonstrates relational persistence.
- React provides a simple operational dashboard.
- Docker makes the environment reproducible.
- GitHub Actions provides visible CI evidence.

## Cloud
Azure is the first deployment target because the architecture maps naturally to containerized services and managed databases. A GCP mapping can be documented separately.
