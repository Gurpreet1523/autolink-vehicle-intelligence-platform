# AutoLink Vehicle Intelligence Platform — End-to-End QA & Cloud Engineering Lab

> Portfolio project inspired by publicly available automotive software/testing job requirements.
> This is an independent simulation and is **not manufacturer proprietary software**.

## What this project demonstrates

- Python + FastAPI REST API development
- PostgreSQL data persistence
- React + TypeScript dashboard
- Virtual ECU / vehicle telemetry simulation
- Pytest unit, API and integration testing
- Requirements traceability and QA documentation
- Locust performance testing
- Stress / soak / stability test scenarios
- Failure injection and root-cause analysis workflow
- Docker / Docker Compose
- GitHub Actions CI/CD
- Terraform-based Azure deployment starter
- Health checks, metrics and structured logging
- Security and code-quality checks

## Architecture

Vehicle Simulator -> FastAPI -> PostgreSQL
                         |
                         +-> React Dashboard
                         |
                         +-> /health and /metrics

CI/CD:
Git push -> lint -> unit/API tests -> integration tests -> security -> Docker build

## Local quick start

Requirements:
- Docker Desktop
- Git
- Python 3.12+ (optional if running tests outside Docker)
- Node.js 20+ (optional if running frontend outside Docker)

```bash
git clone <your-github-repository>
cd autolink-vehicle-intelligence-platform
docker compose up --build
```

Open:
- API docs: http://localhost:8000/docs
- API health: http://localhost:8000/health
- Dashboard: http://localhost:5173

Create sample vehicle:

```bash
curl -X POST http://localhost:8000/vehicles \
  -H "Content-Type: application/json" \
  -d '{"vehicle_id":"VEH-1001","model":"EV-SIM","software_version":"2.4.1"}'
```

Send telemetry:

```bash
curl -X POST http://localhost:8000/telemetry \
  -H "Content-Type: application/json" \
  -d '{"vehicle_id":"VEH-1001","speed":72,"battery":84,"motor_temperature":67.4,"latitude":45.4215,"longitude":-75.6972,"doors_locked":true,"brake_status":"OK","software_version":"2.4.1"}'
```

## Run automated tests

```bash
pip install -r backend/requirements.txt
pytest -q
```

## Run performance tests

Start the API first, then:

```bash
pip install locust
locust -f performance/locustfile.py --host=http://localhost:8000
```

Open http://localhost:8089.

## Project phases

1. Requirements and architecture
2. Backend/API development
3. Virtual ECU simulation
4. Frontend dashboard
5. QA automation
6. Performance, stress, soak and stability testing
7. Failure injection and RCA
8. Docker + CI/CD
9. Cloud + Terraform
10. Portfolio evidence and interview preparation

## Important portfolio rule

Only claim test counts, coverage, latency, throughput and cloud results after actually running the tests. The repository provides the tooling to generate those measurements.
