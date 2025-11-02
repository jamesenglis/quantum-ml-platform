from prometheus_client import Counter, Histogram, Gauge, generate_latest
import time
from loguru import logger

# Define metrics
PREDICTION_COUNTER = Counter('model_predictions_total', 'Total predictions made', ['model_version', 'status'])
PREDICTION_LATENCY = Histogram('prediction_latency_seconds', 'Prediction latency in seconds')
ERROR_COUNTER = Counter('model_errors_total', 'Total prediction errors', ['error_type'])
DRIFT_GAUGE = Gauge('data_drift_score', 'Data drift detection score')

class MetricsCollector:
    def __init__(self):
        self.start_time = time.time()
    
    def record_prediction(self, model_version: str, success: bool = True):
        """Record prediction metrics"""
        status = "success" if success else "failure"
        PREDICTION_COUNTER.labels(model_version=model_version, status=status).inc()
    
    def record_latency(self, latency: float):
        """Record prediction latency"""
        PREDICTION_LATENCY.observe(latency)
    
    def record_error(self, error_type: str):
        """Record error metrics"""
        ERROR_COUNTER.labels(error_type=error_type).inc()
    
    def record_drift(self, drift_score: float):
        """Record data drift metrics"""
        DRIFT_GAUGE.set(drift_score)
    
    def get_metrics(self):
        """Get all metrics in Prometheus format"""
        return generate_latest()

metrics_collector = MetricsCollector()
