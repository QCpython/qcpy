from qcpy import quantumcircuit

# Create Quantum Circuit class object of 2 qubits and represent the placement of values in little_endian format.
qc = quantumcircuit(qubits = 2, little_endian = True)

# Call the hadamard gate and have it be placed on qubit 0.
qc.hadamard(0)
# Print the state of the quantum circuit.
print(qc.state())