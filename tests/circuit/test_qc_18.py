from QCpy import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    qc.hadamard(x - 1)
    qc.hadamard(x - 2)
    qc.hadamard(x - 3)
    qc.rc3x(x - 1, x - 2, x - 3, 0)
    return qc.state()

def test_18a():
    assert (inc(4) == np.array([ 0.354+0j, 0+0j, 0.354+0j, 0+0j, 0.354+0j, 0+0j, 0.354+0j, 0+0j, 0.354+0j, 0+0j, 0.354+0j, 0+0j, 0+0.354j, 0+0j, 0+0j, -0.354+0j ], 'F').reshape(16, 1)).all(), "test_18a Failed"
def test_18b():
    assert (inc(5) == np.array([ 0.354+0j, 0+0j, 0+0j, 0+0j, 0.354+0j, 0+0j, 0+0j, 0+0j, 0.354+0j, 0+0j, 0+0j, 0+0j, 0.354+0j, 0+0j, 0+0j, 0+0j, 0.354+0j, 0+0j, 0+0j, 0+0j, 0.354+0j, 0+0j, 0+0j, 0+0j, 0+0.354j, 0+0j, 0+0j, 0+0j, 0+0j, -0.354+0j, 0+0j, 0+0j ], 'F').reshape(32, 1)).all(), "test_18b Failed"