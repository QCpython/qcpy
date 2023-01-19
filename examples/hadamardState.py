from QCpy import QuantumCircuit

number_of_qubits = 3
# Create Quantum Circuit class object of 2 qubits and represent the placement of values in little_endian format.
qc = QuantumCircuit(qubits = number_of_qubits, little_endian = True, prep = 'z')

# Enact the hadamard gate on each and every qubit in the quantum circuit.
for i in range(number_of_qubits):
    qc.hadamard(i)
# Print the probabilites of the quantum circuit.
print(qc.probabilities())



