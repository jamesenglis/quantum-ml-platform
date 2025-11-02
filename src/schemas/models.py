from pydantic import BaseModel
from typing import List, Optional

class PredictionRequest(BaseModel):
    features: List[float]
    model_version: Optional[str] = "latest"

class PredictionResponse(BaseModel):
    prediction: List[float]
    confidence: float
    model_version: str
    inference_time: float

class ModelInfo(BaseModel):
    name: str
    version: str
    status: str
    performance: dict
