"""
Simple Qiskit tests for minimal setup
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_qiskit_import():
    """Test that Qiskit imports work"""
    from qiskit import QuantumCircuit
    from qiskit.quantum_info import Statevector
    assert True

def test_quantum_circuit():
    """Test basic quantum circuit creation"""
    from qiskit import QuantumCircuit
    
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    
    assert qc.num_qubits == 2

def test_statevector_simulation():
    """Test statevector simulation"""
    from qiskit import QuantumCircuit
    from qiskit.quantum_info import Statevector
    
    qc = QuantumCircuit(2)
    qc.h(0)
    
    statevector = Statevector.from_instruction(qc)
    counts = statevector.sample_counts(shots=100)
    
    assert isinstance(counts, dict)
    assert len(counts) > 0

def test_our_quantum_manager():
    """Test our quantum manager module"""
    from src.circuits.quantum_manager import QuantumCircuitManager
    qm = QuantumCircuitManager(n_qubits=2)
    circuit = qm.create_encoding_circuit([0.1, 0.2])
    assert circuit.num_qubits == 2
