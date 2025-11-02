"""
Quantum MLOps Integration
Industry-standard experiment tracking, model management, and workflow orchestration
"""
import logging
import os
from typing import Dict, Any, Optional
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

class QuantumMLOpsManager:
    """
    Industry-standard MLOps integration for quantum machine learning
    """
    
    def __init__(self, 
                 experiment_name: str = "quantum-ml-experiments",
                 tracking_uri: str = "./mlruns",
                 wandb_project: str = "quantum-ml-platform",
                 enable_wandb: bool = False):
        
        self.experiment_name = experiment_name
        self.tracking_uri = tracking_uri
        self.wandb_project = wandb_project
        self.enable_wandb = enable_wandb
        
        # Set environment variable to disable WandB prompts
        os.environ["WANDB_SILENT"] = "true"
        os.environ["WANDB_DISABLE_CODE"] = "true"
        
        # Try to import MLflow (optional dependency)
        try:
            import mlflow
            from mlflow.tracking import MlflowClient
            mlflow.set_tracking_uri(tracking_uri)
            mlflow.set_experiment(experiment_name)
            self.mlflow_client = MlflowClient()
            self.mlflow_available = True
        except ImportError:
            self.mlflow_available = False
            logger.warning("MLflow not available - running in local mode")
        
        # Try to import WandB (optional dependency)
        self.wandb_available = False
        if self.enable_wandb:
            try:
                import wandb
                # Try to initialize in offline mode to avoid prompts
                try:
                    wandb.init(project=wandb_project, reinit=True, mode="offline")
                    self.wandb_available = True
                except:
                    # If offline fails, try without initialization
                    self.wandb_available = False
                    logger.warning("Weights & Biases initialization failed - running without it")
            except ImportError:
                self.wandb_available = False
                logger.warning("Weights & Biases not available")
        
        self._setup_directories()
        logger.info(f"QuantumMLOpsManager initialized for experiment: {experiment_name}")
        logger.info(f"MLflow available: {self.mlflow_available}")
        logger.info(f"WandB available: {self.wandb_available}")
    
    def _setup_directories(self):
        """Create necessary directories for MLOps"""
        Path(self.tracking_uri).mkdir(exist_ok=True)
        Path("models").mkdir(exist_ok=True)
        Path("experiments").mkdir(exist_ok=True)
    
    def start_experiment(self, 
                        run_name: str = None,
                        tags: Dict[str, str] = None,
                        description: str = None) -> str:
        """
        Start a new quantum experiment with comprehensive tracking
        """
        if run_name is None:
            run_name = f"quantum_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Start MLflow run if available
        if self.mlflow_available:
            import mlflow
            mlflow.start_run(run_name=run_name)
            
            # Set tags
            if tags:
                mlflow.set_tags(tags)
            
            # Log description
            if description:
                mlflow.set_tag("description", description)
            
            # Log system info
            self._log_system_info()
            
            run_id = mlflow.active_run().info.run_id
        else:
            # Local mode - just create a run ID
            run_id = f"local_{run_name}"
        
        logger.info(f"Started experiment: {run_name}")
        return run_id
    
    def log_quantum_parameters(self, 
                             circuit_params: Dict[str, Any],
                             training_params: Dict[str, Any],
                             model_params: Dict[str, Any]):
        """
        Log comprehensive quantum experiment parameters
        """
        # Log to MLflow if available
        if self.mlflow_available:
            import mlflow
            mlflow.log_params({
                **{f"circuit_{k}": v for k, v in circuit_params.items()},
                **{f"training_{k}": v for k, v in training_params.items()},
                **{f"model_{k}": v for k, v in model_params.items()}
            })
        
        # Log to wandb if available
        if self.wandb_available:
            try:
                import wandb
                wandb.config.update({
                    "circuit_params": circuit_params,
                    "training_params": training_params,
                    "model_params": model_params
                })
            except:
                # Silently fail if WandB has issues
                pass
    
    def log_quantum_metrics(self, 
                          metrics: Dict[str, float],
                          step: int = None,
                          phase: str = "training"):
        """
        Log quantum-specific metrics with phase tracking
        """
        # Log to MLflow if available
        if self.mlflow_available:
            import mlflow
            mlflow.log_metrics({f"{phase}_{k}": v for k, v in metrics.items()}, step=step)
        
        # Log to wandb if available
        if self.wandb_available:
            try:
                import wandb
                wandb.log({f"{phase}_{k}": v for k, v in metrics.items()}, step=step)
            except:
                # Silently fail if WandB has issues
                pass
    
    def _log_system_info(self):
        """Log system and environment information"""
        if not self.mlflow_available:
            return
            
        import platform
        import sys
        import mlflow
        
        system_info = {
            "python_version": sys.version,
            "platform": platform.platform(),
            "processor": platform.processor()
        }
        
        # Add version info for available packages
        try:
            system_info["mlflow_version"] = mlflow.__version__
        except:
            pass
            
        try:
            import wandb
            system_info["wandb_version"] = wandb.__version__
        except:
            pass
        
        mlflow.set_tags({f"system_{k}": v for k, v in system_info.items()})
    
    def end_experiment(self):
        """End the current experiment"""
        if self.mlflow_available:
            import mlflow
            mlflow.end_run()
        
        if self.wandb_available:
            try:
                import wandb
                wandb.finish()
            except:
                # Silently fail if WandB has issues
                pass
        
        logger.info("Experiment completed")

# Example usage and testing
if __name__ == "__main__":
    # Initialize MLOps manager WITHOUT WandB to avoid prompts
    mlops = QuantumMLOpsManager(enable_wandb=False)
    
    # Start experiment
    run_id = mlops.start_experiment(
        run_name="demo_quantum_experiment",
        tags={"phase": "development", "quantum_framework": "qiskit"},
        description="Demo quantum experiment with MLOps integration"
    )
    
    try:
        # Log parameters
        circuit_params = {
            "n_qubits": 4,
            "n_layers": 2,
            "entanglement": "linear"
        }
        
        training_params = {
            "learning_rate": 0.01,
            "epochs": 100,
            "batch_size": 32
        }
        
        model_params = {
            "observable": "pauli_z",
            "shots": 1000
        }
        
        mlops.log_quantum_parameters(circuit_params, training_params, model_params)
        
        # Simulate logging metrics
        for epoch in range(3):
            metrics = {
                "loss": 1.0 / (epoch + 1),
                "accuracy": 0.8 + epoch * 0.05,
                "expectation": 0.5 + epoch * 0.1
            }
            mlops.log_quantum_metrics(metrics, step=epoch)
            print(f"Logged metrics for epoch {epoch}: {metrics}")
        
        print("✅ MLOps integration demo completed successfully!")
        
    finally:
        mlops.end_experiment()
