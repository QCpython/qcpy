from qiskit import QuantumCircuit, QuantumRegister, Aer, execute

# Create a Quantum Register with 50 qubits
qreg = QuantumRegister(29, 'q')

# Create a Quantum Circuit using the Quantum Register
qc = QuantumCircuit(qreg)

# Perform some operations on the qubits
qc.h(qreg[0])
qc.cx(qreg[0], qreg[1])

# Get the statevector using the statevector simulator
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
statevector = result.get_statevector(qc)

# Print the statevector
print(statevector)

