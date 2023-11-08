from qcpy import quantumcircuit

# Create Quantum Circuit class object of 2 qubits and represent the placement of values in little_endian format.
qc = quantumcircuit(qubits=2, prep="z", little_endian=True)

# Call the hadamard gate and have it be placed on qubit 0.
qc.h(0)
# Call the CNOT gate and have the control be qubit 0 and the target be qubit 1.
qc.cnot(0, 1)
# Call the hadamard gate and have it be placed on qubit 0.
qc.h(0)
# Print the state of the quantum circuit.
print(qc.state)
