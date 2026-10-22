import os
import random
import time
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000")
VEHICLE_ID = os.getenv("VEHICLE_ID", "VEH-1001")
INTERVAL = float(os.getenv("INTERVAL_SECONDS", "2"))

def ensure_vehicle():
    payload = {
        "vehicle_id": VEHICLE_ID,
        "model": "EV-SIM",
        "software_version": "2.4.1"
    }
    response = requests.post(f"{API_URL}/vehicles", json=payload, timeout=5)
    if response.status_code not in (201, 409):
        response.raise_for_status()

def read_sensors():
    return {
        "vehicle_id": VEHICLE_ID,
        "speed": round(random.uniform(0, 120), 1),
        "battery": round(random.uniform(20, 100), 1),
        "motor_temperature": round(random.uniform(40, 95), 1),
        "latitude": 45.4215 + random.uniform(-0.01, 0.01),
        "longitude": -75.6972 + random.uniform(-0.01, 0.01),
        "doors_locked": True,
        "brake_status": "OK",
        "software_version": "2.4.1"
    }

def main():
    while True:
        try:
            ensure_vehicle()
            response = requests.post(
                f"{API_URL}/telemetry",
                json=read_sensors(),
                timeout=5
            )
            print(response.status_code, response.text)
        except Exception as exc:
            print("ECU communication failure:", exc)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
