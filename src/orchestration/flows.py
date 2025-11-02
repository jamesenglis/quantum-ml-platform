from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
import mlflow
from loguru import logger
import time

@task
def load_data_task():
    """Task to load and preprocess data"""
    logger.info("Loading data...")
    time.sleep(1)  # Simulate work
    return "data_loaded"

@task
def preprocess_data_task(data):
    """Task to preprocess data"""
    logger.info("Preprocessing data...")
    time.sleep(1)
    return "data_preprocessed"

@task
def train_model_task(data):
    """Task to train model"""
    logger.info("Training model...")
    time.sleep(2)
    
    # Mock MLflow tracking
    logger.info("Logging to MLflow...")
    return "model_trained"

@task
def evaluate_model_task(model):
    """Task to evaluate model"""
    logger.info("Evaluating model...")
    time.sleep(1)
    return {"accuracy": 0.95, "loss": 0.1}

@flow(name="quantum-ml-training-flow", task_runner=SequentialTaskRunner())
def training_flow():
    """Main training workflow"""
    logger.info("Starting Quantum ML Training Flow")
    
    # Execute tasks in order
    data = load_data_task()
    processed_data = preprocess_data_task(data)
    model = train_model_task(processed_data)
    evaluation = evaluate_model_task(model)
    
    logger.info(f"Training completed with metrics: {evaluation}")
    return evaluation

@flow(name="model-serving-flow")
def serving_flow():
    """Model serving and deployment workflow"""
    logger.info("Starting model serving workflow...")
    time.sleep(1)
    logger.info("Model serving completed")
    return "serving_complete"

if __name__ == "__main__":
    # Run the flow directly for testing
    result = training_flow()
    print(f"Flow result: {result}")
