"""
Tests for Quantum MLOps Integration
"""
import pytest
import tempfile
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestQuantumMLOps:
    """Test Quantum MLOps functionality"""
    
    def test_import(self):
        """Test that MLOps modules can be imported"""
        from src.utils.quantum_mlops import QuantumMLOpsManager
        assert True
    
    def test_mlops_initialization(self):
        """Test MLOps manager initialization"""
        with tempfile.TemporaryDirectory() as tmpdir:
            from src.utils.quantum_mlops import QuantumMLOpsManager
            
            mlops = QuantumMLOpsManager(
                experiment_name="test_experiment",
                tracking_uri=tmpdir
            )
            
            assert mlops.experiment_name == "test_experiment"
            assert mlops.tracking_uri == tmpdir
    
    def test_experiment_lifecycle(self):
        """Test complete experiment lifecycle"""
        with tempfile.TemporaryDirectory() as tmpdir:
            from src.utils.quantum_mlops import QuantumMLOpsManager
            
            mlops = QuantumMLOpsManager(tracking_uri=tmpdir)
            
            # Start experiment
            run_id = mlops.start_experiment(
                run_name="test_run",
                tags={"test": "true"},
                description="Test experiment"
            )
            
            # Log parameters
            circuit_params = {"n_qubits": 2, "n_layers": 1}
            training_params = {"learning_rate": 0.01}
            model_params = {"observable": "pauli_z"}
            
            mlops.log_quantum_parameters(circuit_params, training_params, model_params)
            
            # Log metrics
            metrics = {"loss": 0.5, "accuracy": 0.8}
            mlops.log_quantum_metrics(metrics, step=0)
            
            # End experiment
            mlops.end_experiment()
            
            assert run_id is not None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
