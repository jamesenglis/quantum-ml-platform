from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import time
from loguru import logger

from src.schemas.models import PredictionRequest, PredictionResponse, ModelInfo
from src.models.model_manager import model_manager

app = FastAPI(
    title="Quantum ML Platform API",
    description="Production API for Quantum Machine Learning Models",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Initialize model on startup"""
    try:
        # Load a sample model - replace with your actual model path
        # model_manager.load_model("models/sample_model.pkl", "quantum_model")
        logger.info("API startup completed - Model loading disabled for demo")
    except Exception as e:
        logger.error(f"Startup error: {e}")

@app.get("/")
async def root():
    return {"message": "Quantum ML Platform API", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": time.time()}

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Make predictions using the quantum ML model"""
    start_time = time.time()
    
    try:
        # Demo prediction - replace with actual model inference
        mock_prediction = [sum(request.features) / len(request.features)] if request.features else [0.0]
        inference_time = time.time() - start_time
        
        return PredictionResponse(
            prediction=mock_prediction,
            confidence=0.95,
            model_version=request.model_version or "latest",
            inference_time=inference_time
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/models/{model_name}")
async def get_model_info(model_name: str):
    """Get information about a specific model"""
    return ModelInfo(
        name=model_name,
        version="1.0.0",
        status="loaded",
        performance={"accuracy": 0.95, "loss": 0.1}
    )

@app.get("/models")
async def list_models():
    """List all available models"""
    return {
        "models": list(model_manager.models.keys()),
        "current_model": model_manager.current_model
    }
