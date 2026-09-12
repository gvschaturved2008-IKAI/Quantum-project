from qiskit import QuantumCircuit

# Create a quantum circuit containing one qubit
qc = QuantumCircuit(1)

# Apply a Hadamard gate to the qubit
qc.h(0)

# Display the circuit
print(qc)