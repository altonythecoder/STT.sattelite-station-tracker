# schemas.py
from pydantic import BaseModel, Field
from typing import Optional, List

class PassPrediction(BaseModel):
    AOS: str = Field(..., description="Sinyal Yakalama Zamanı (UTC ISO)")
    MAX_ELEVATION_TIME: Optional[str] = Field(None, description="En Yüksek Yükselim Açısı Zamanı (UTC ISO)")
    MAX_ELEVATION_DEG: Optional[float] = Field(None, description="En Yüksek Yükselim Açısı (°)")
    MAX_ELEVATION_AZIMUTH_DEG: Optional[float] = Field(None, description="En Yüksek Açı Anındaki Azimut (°)")
    LOS: Optional[str] = Field(None, description="Sinyal Kaybı Zamanı (UTC ISO)")

class PassPredictionResponse(BaseModel):
    norad_id: int
    satellite_name: str
    ground_station: dict
    passes_count: int
    passes: List[PassPrediction]

class LiveSatelliteTelemetry(BaseModel):
    satellite_name: str
    norad_id: int
    timestamp_utc: str
    latitude: float
    longitude: float
    altitude_km: float
    azimuth_deg: Optional[float] = Field(None, description="Yer istasyonuna göre açı")
    elevation_deg: Optional[float] = Field(None, description="Yer istasyonuna göre dikey yükselim açısı")
    distance_km: Optional[float] = Field(None, description="Yer istasyonuna olan kuşuçuşu mesafe")