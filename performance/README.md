# Performance Testing

## Smoke
10 users for 1 minute.

## Load
100 users for 10 minutes.

## Stress
Increase users in steps:
100 -> 250 -> 500 -> 1000.

Record:
- requests/second
- average response time
- p95/p99
- error percentage
- CPU/memory
- database behavior

## Soak
Run a stable workload for 2+ hours.

Look for:
- memory growth
- connection leaks
- increasing latency
- error accumulation

Do not publish example numbers as real results. Replace them with measured output.
