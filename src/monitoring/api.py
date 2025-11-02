from fastapi import APIRouter, Response
from src.monitoring.monitor import monitor
from src.monitoring.metrics import metrics_collector

router = APIRouter(prefix="/monitoring", tags=["monitoring"])

@router.get("/health")
async def monitoring_health():
    return {"status": "healthy", "service": "monitoring"}

@router.get("/metrics")
async def get_metrics():
    """Prometheus metrics endpoint"""
    metrics = metrics_collector.get_metrics()
    return Response(media_type="text/plain", content=metrics)

@router.get("/drift")
async def check_drift():
    """Check for data drift"""
    # This would use actual data in production
    import pandas as pd
    import numpy as np
    
    # Sample data for demonstration
    reference_data = pd.DataFrame({
        'feature1': np.random.normal(0, 1, 100),
        'feature2': np.random.normal(5, 2, 100)
    })
    
    current_data = pd.DataFrame({
        'feature1': np.random.normal(0.1, 1, 50),  # Slight drift
        'feature2': np.random.normal(5, 2, 50)
    })
    
    drift_report = monitor.check_data_drift(current_data, reference_data)
    return drift_report

@router.get("/performance")
async def get_performance():
    """Get model performance metrics"""
    performance_report = monitor.generate_performance_report()
    return performance_report
