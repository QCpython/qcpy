from QCpy import QuantumCircuit

# Create Quantum Circuit class object of 2 qubits and represent the placement of values in little_endian format.
qc = QuantumCircuit(qubits = 2, little_endian = True)

# Print the state of quantum circuit.
print(qc.state())
