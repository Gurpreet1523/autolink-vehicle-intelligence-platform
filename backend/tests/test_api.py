def vehicle_payload():
    return {"vehicle_id":"VEH-TEST","model":"EV-SIM","software_version":"1.0.0"}

def telemetry_payload():
    return {
        "vehicle_id":"VEH-TEST","speed":72,"battery":84,
        "motor_temperature":67.4,"latitude":45.4215,
        "longitude":-75.6972,"doors_locked":True,
        "brake_status":"OK","software_version":"1.0.0"
    }

def test_create_vehicle(client):
    response = client.post("/vehicles", json=vehicle_payload())
    assert response.status_code == 201
    assert response.json()["vehicle_id"] == "VEH-TEST"

def test_duplicate_vehicle_rejected(client):
    client.post("/vehicles", json=vehicle_payload())
    response = client.post("/vehicles", json=vehicle_payload())
    assert response.status_code == 409

def test_unknown_vehicle_rejected(client):
    response = client.post("/telemetry", json=telemetry_payload())
    assert response.status_code == 404

def test_valid_telemetry(client):
    client.post("/vehicles", json=vehicle_payload())
    response = client.post("/telemetry", json=telemetry_payload())
    assert response.status_code == 201
    assert response.json()["battery"] == 84

def test_invalid_battery_rejected(client):
    client.post("/vehicles", json=vehicle_payload())
    payload = telemetry_payload()
    payload["battery"] = 101
    response = client.post("/telemetry", json=payload)
    assert response.status_code == 422

def test_negative_speed_rejected(client):
    client.post("/vehicles", json=vehicle_payload())
    payload = telemetry_payload()
    payload["speed"] = -1
    response = client.post("/telemetry", json=payload)
    assert response.status_code == 422

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
