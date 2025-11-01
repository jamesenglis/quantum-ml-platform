import pennylane as qml
import numpy as np

class BasicCircuits:
    """Collection of basic parameterized quantum circuits"""
    
    def __init__(self, n_qubits=4):
        self.n_qubits = n_qubits
        
    def create_penny_lane_circuit(self, inputs, weights):
        """Create a basic variational circuit in PennyLane"""
        dev = qml.device("default.qubit", wires=self.n_qubits)
        
        @qml.qnode(dev)
        def circuit(inputs, weights):
            # Encode input data
            for i in range(self.n_qubits):
                qml.RY(inputs[i], wires=i)
            
            # Variational layers
            for layer in range(len(weights)):
                # Entangling layer
                for i in range(self.n_qubits - 1):
                    qml.CNOT(wires=[i, i + 1])
                
                # Rotation layer
                for i in range(self.n_qubits):
                    qml.RY(weights[layer][i], wires=i)
            
            return qml.expval(qml.PauliZ(0))
        
        return circuit(inputs, weights)

# Test the configuration
if __name__ == "__main__":
    circuit = BasicCircuits(n_qubits=2)
    inputs = np.array([0.1, 0.2])
    weights = np.array([[0.3, 0.4]])
    result = circuit.create_penny_lane_circuit(inputs, weights)
    print(f"Circuit test result: {result}")
