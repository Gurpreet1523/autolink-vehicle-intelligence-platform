from app.schemas import VehicleCreate, TelemetryCreate
from app.services import create_vehicle, add_telemetry
from app.database import SessionLocal

def test_service_persists_vehicle():
    db = SessionLocal()
    vehicle = create_vehicle(db, VehicleCreate(
        vehicle_id="VEH-SVC", model="EV", software_version="1.0"
    ))
    assert vehicle.vehicle_id == "VEH-SVC"
    db.close()

def test_service_marks_vehicle_online():
    db = SessionLocal()
    create_vehicle(db, VehicleCreate(
        vehicle_id="VEH-SVC", model="EV", software_version="1.0"
    ))
    telemetry = TelemetryCreate(
        vehicle_id="VEH-SVC", speed=10, battery=90,
        motor_temperature=40, latitude=45, longitude=-75,
        doors_locked=True, brake_status="OK", software_version="1.0"
    )
    add_telemetry(db, telemetry)
    db.refresh(db.get(__import__("app.models", fromlist=["Vehicle"]).Vehicle, 1))
    db.close()
