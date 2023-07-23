from qcpy import quantumcircuit
from qcpy.visualizer import StateVector
import numpy as np
circuit = quantumcircuit(5, little_endian = True)
circuit.hadamard(0)
circuit.hadamard(1)
circuit.hadamard(2)
circuit.hadamard(3)
circuit.hadamard(4)

circuit.cnot(0,1)
circuit.toffoli(0,1,2)
circuit.t(1)
circuit.t(2)
circuit.hadamard(1)
circuit.hadamard(2)
circuit.z(3)
circuit.toffoli(0, 2, 1)
circuit.sdg(2)
circuit.u(2, np.pi / 2)
circuit.rz(4)

test = StateVector(circuit)
test.makeGraph(save=False, show=True, darkmode=True)