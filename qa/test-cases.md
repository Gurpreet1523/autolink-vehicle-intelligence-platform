# Test Cases

| ID | Scenario | Expected |
|---|---|---|
| TC-001 | Create valid vehicle | 201 |
| TC-002 | Create duplicate vehicle | 409 |
| TC-003 | Send telemetry for registered vehicle | 201 |
| TC-004 | Send telemetry for unknown vehicle | 404 |
| TC-005 | Battery -1 | 422 |
| TC-006 | Battery 101 | 422 |
| TC-007 | Speed -1 | 422 |
| TC-008 | Speed 0 | Accepted |
| TC-009 | Speed 300 | Accepted |
| TC-010 | Speed >300 | 422 |
| TC-011 | Missing required telemetry field | 422 |
| TC-012 | Health endpoint | 200 + healthy |
| TC-013 | Retrieve latest telemetry | 200 |
| TC-014 | Duplicate registration under concurrency | No duplicate records |
| TC-015 | API recovers after restart | Health returns healthy |
