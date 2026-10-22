from datetime import datetime
from pydantic import BaseModel, Field

class VehicleCreate(BaseModel):
    vehicle_id: str = Field(min_length=3, max_length=50)
    model: str
    software_version: str

class VehicleResponse(VehicleCreate):
    status: str
    created_at: datetime
    model_config = {"from_attributes": True}

class TelemetryCreate(BaseModel):
    vehicle_id: str
    speed: float = Field(ge=0, le=300)
    battery: float = Field(ge=0, le=100)
    motor_temperature: float = Field(ge=-40, le=200)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    doors_locked: bool
    brake_status: str
    software_version: str

class TelemetryResponse(TelemetryCreate):
    id: int
    timestamp: datetime
    model_config = {"from_attributes": True}

class DiagnosticCreate(BaseModel):
    vehicle_id: str
    error_code: str
    severity: str
    description: str
