from qcpy import quantumcircuit, u

# Create Quantum Circuit class object of 3 qubits and represent the placement of values in little_endian format.
qc = quantumcircuit(qubits=2, little_endian=True)

# Create variable to store matrix representation of the U gate.
u = u()
# Call the hadamard gate and have it be placed on qubit 0.
qc.h(0)
# Call to the customControlPhase, which will use qubit 0 as a control and qubit 1 as a target
# the matrix in the U gate is then used to designate what will be enacted on the qubits.
qc.customcontrolled(0, 1, u)
print(qc.state())
