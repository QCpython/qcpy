from qcpy import quantumcircuit



print(quantumcircuit(qubits = 4, little_endian=True, prep='z').state())
