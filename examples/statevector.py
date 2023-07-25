from qcpy import quantumcircuit
from qcpy.visualizer import statevector
import numpy as np
circuit = quantumcircuit(5, little_endian = True)
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)
circuit.h(4)

circuit.cnot(0,1)
circuit.toffoli(0,1,2)
circuit.t(1)
circuit.t(2)
circuit.h(1)
circuit.h(2)
circuit.z(3)
circuit.toffoli(0, 2, 1)
circuit.sdg(2)
circuit.u(2, np.pi / 2)
circuit.rz(4)

test = statevector(circuit)
test.make(save=False, show=True, darkmode=True)