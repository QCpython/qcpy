from qcpy import qsphere, quantumcircuit

# creates a circuitfor 3 qubits
qc = quantumcircuit(3)
# call the hadamard gate on all 3 qubits
qc.h(0)
qc.h(1)
qc.h(2)
# call the QSphere class on the circuit
sphere_test = qsphere(qc)
# call the makeSphere method, this will show the sphere in a new window
sphere_test.make(save=False, show=True)
