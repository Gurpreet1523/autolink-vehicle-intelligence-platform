from locust import HttpUser, task, between
import random

class VehicleTelemetryUser(HttpUser):
    wait_time = between(0.2, 1.0)

    @task(5)
    def send_telemetry(self):
        vehicle_id = f"LOAD-{random.randint(1, 1000)}"
        payload = {
            "vehicle_id": vehicle_id,
            "speed": random.uniform(0, 120),
            "battery": random.uniform(20, 100),
            "motor_temperature": random.uniform(40, 95),
            "latitude": 45.4215,
            "longitude": -75.6972,
            "doors_locked": True,
            "brake_status": "OK",
            "software_version": "2.4.1"
        }
        # In a realistic load test, pre-provision these vehicles or add
        # a setup task before telemetry generation.
        self.client.post("/telemetry", json=payload, name="/telemetry")
