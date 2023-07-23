from qcpy import quantumcircuit

# Create Quantum Circuit class object of 3 qubits and represent the placement of values in little_endian format.
qc = quantumcircuit(qubits = 3, little_endian = True)

# Call the hadamard gate and have it be placed on qubit 0.
qc.hadamard(0)
# Call the hadamard gate and have it be placed on qubit 1.
qc.hadamard(1)
# Call to the Toffoli gate where the qubits 0 and 1 are control qubits, and qubit 2 is the target.
qc.toffoli(0,1,2)
# Print the state of quantum circuit.
print(qc.state())
