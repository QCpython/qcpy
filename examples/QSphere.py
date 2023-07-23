from qcpy import quantumcircuit
from qcpy.visualizer import QSphere

# creates a circuitfor 3 qubits
qc = quantumcircuit(3)
# call the hadamard gate on all 3 qubits
qc.hadamard(0)
qc.hadamard(1)
qc.hadamard(2)
# call the QSphere class on the circuit
sphere_test = QSphere(qc)
# call the makeSphere method, this will show the sphere in a new window
sphere_test.makeSphere(save=False, show=True)