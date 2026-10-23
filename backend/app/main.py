import logging
from fastapi import Depends, FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .schemas import VehicleCreate, VehicleResponse, TelemetryCreate, TelemetryResponse, DiagnosticCreate
from .services import create_vehicle, get_vehicle, add_telemetry, get_telemetry, add_diagnostic

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vehicle-platform")

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Connected Vehicle Platform API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://10.0.0.170:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "healthy", "service": "vehicle-api"}

@app.get("/metrics")
def metrics():
    return {"service": "vehicle-api", "metrics": "Use application/cloud metrics in production"}

@app.post("/vehicles", response_model=VehicleResponse, status_code=201)
def post_vehicle(data: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db, data)

@app.get("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def read_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    return get_vehicle(db, vehicle_id)

@app.post("/telemetry", response_model=TelemetryResponse, status_code=201)
def post_telemetry(data: TelemetryCreate, db: Session = Depends(get_db)):
    return add_telemetry(db, data)

@app.get("/vehicles/{vehicle_id}/telemetry", response_model=list[TelemetryResponse])
def read_telemetry(
    vehicle_id: str,
    limit: int = Query(default=50, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return get_telemetry(db, vehicle_id, limit)

@app.post("/diagnostics", status_code=201)
def post_diagnostic(data: DiagnosticCreate, db: Session = Depends(get_db)):
    return add_diagnostic(db, data)
