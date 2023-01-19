from QCpy import QuantumCircuit

# Create Quantum Circuit class object of 2 qubits and represent the placement of values in little_endian format.
qc = QuantumCircuit(qubits = 2,little_endian = True, prep = 'z')

# Call the hadamard gate and have it be placed on qubit 0.
qc.hadamard(0)
# Call the swap gate to switch the values of qubit 0 and qubit 1.
qc.swap(0,1)
# Print the state of the quantum circuit.
print(qc.state())
