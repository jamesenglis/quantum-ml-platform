#!/usr/bin/env python3
"""
Simple test for MLOps integration
"""
import sys
import os
sys.path.insert(0, '.')

def test_mlops_basic():
    print("🧪 Testing MLOps Basic Functionality")
    print("=" * 40)
    
    # Test import
    try:
        from src.utils.quantum_mlops import QuantumMLOpsManager
        print("✅ Import successful")
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    
    # Test initialization
    try:
        mlops = QuantumMLOpsManager(enable_wandb=False)
        print("✅ Initialization successful")
        print(f"   MLflow: {mlops.mlflow_available}")
        print(f"   WandB: {mlops.wandb_available}")
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        return False
    
    # Test experiment lifecycle
    try:
        run_id = mlops.start_experiment(run_name="test_run")
        print("✅ Experiment start successful")
        
        # Log some parameters
        mlops.log_quantum_parameters(
            {"n_qubits": 2}, 
            {"learning_rate": 0.01}, 
            {"observable": "Z"}
        )
        print("✅ Parameter logging successful")
        
        # Log some metrics
        mlops.log_quantum_metrics({"loss": 0.5, "accuracy": 0.8})
        print("✅ Metric logging successful")
        
        mlops.end_experiment()
        print("✅ Experiment end successful")
        
    except Exception as e:
        print(f"❌ Experiment lifecycle failed: {e}")
        return False
    
    print("")
    print("🎉 All MLOps tests passed!")
    return True

if __name__ == "__main__":
    success = test_mlops_basic()
    sys.exit(0 if success else 1)
