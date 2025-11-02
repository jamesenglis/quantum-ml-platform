from prefect.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule
from datetime import timedelta
from src.orchestration.flows import training_flow, serving_flow

def create_deployments():
    """Create Prefect deployments"""
    
    # Training deployment
    training_deployment = Deployment.build_from_flow(
        flow=training_flow,
        name="quantum-ml-training",
        schedule=IntervalSchedule(interval=timedelta(hours=1)),
        work_pool_name="default"
    )
    
    # Serving deployment
    serving_deployment = Deployment.build_from_flow(
        flow=serving_flow,
        name="model-serving",
        work_pool_name="default"
    )
    
    training_deployment.apply()
    serving_deployment.apply()
    print("Deployments created successfully!")

if __name__ == "__main__":
    create_deployments()
