from QCpy import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    qc.hadamard(0)
    qc.rzz(0, x - 1)
    qc.hadamard(0)
    return qc.state()

def test_19a():
    assert (inc(2) == np.array([ 0.707+0j, 0-0.707j, 0+0j, 0+0j ], 'F').reshape(4, 1)).all(), "test_19a Failed"
def test_19b():
    assert (inc(3) == np.array([ 0.707+0j, 0-0.707j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j ], 'F').reshape(8, 1)).all(), "test_19b Failed"
def test_19c():
    assert (inc(4) == np.array([ 0.707+0j, 0-0.707j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j ], 'F').reshape(16, 1)).all(), "test_19c Failed"
