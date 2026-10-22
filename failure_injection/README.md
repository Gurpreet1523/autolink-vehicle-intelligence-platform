# Failure Injection

Use these scenarios in a controlled local environment:

1. Stop PostgreSQL.
2. Restart the API.
3. Introduce invalid telemetry.
4. Add artificial API latency.
5. Simulate vehicle disconnect/reconnect.

For every experiment capture:
- timestamp
- command/action
- expected behavior
- observed behavior
- logs
- metrics
- recovery time
- RCA
- regression result

Do not run destructive experiments against production resources.
