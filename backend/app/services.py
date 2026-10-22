from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Vehicle, Telemetry, Diagnostic
from .schemas import VehicleCreate, TelemetryCreate, DiagnosticCreate

def create_vehicle(db: Session, data: VehicleCreate):
    if db.scalar(select(Vehicle).where(Vehicle.vehicle_id == data.vehicle_id)):
        raise HTTPException(status_code=409, detail="Vehicle already exists")
    vehicle = Vehicle(**data.model_dump())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def get_vehicle(db: Session, vehicle_id: str):
    vehicle = db.scalar(select(Vehicle).where(Vehicle.vehicle_id == vehicle_id))
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

def add_telemetry(db: Session, data: TelemetryCreate):
    vehicle = get_vehicle(db, data.vehicle_id)
    vehicle.status = "ONLINE"
    telemetry = Telemetry(**data.model_dump())
    db.add(telemetry)
    db.commit()
    db.refresh(telemetry)
    return telemetry

def get_telemetry(db: Session, vehicle_id: str, limit: int = 50):
    get_vehicle(db, vehicle_id)
    return list(db.scalars(
        select(Telemetry).where(Telemetry.vehicle_id == vehicle_id)
        .order_by(Telemetry.timestamp.desc()).limit(limit)
    ))

def add_diagnostic(db: Session, data: DiagnosticCreate):
    get_vehicle(db, data.vehicle_id)
    item = Diagnostic(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
