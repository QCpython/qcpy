from QCpy import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    qc.hadamard(0)
    qc.hadamard(1)
    qc.toffoli(0,1,x - 1)
    return qc.state()

def test_08a():
    assert (inc(3) == np.array([ 0.5+0j, 0.5+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0.5+0j ], 'F').reshape(8, 1)).all(), "test_08a Failed"
def test_08b():
    assert (inc(4) == np.array([ 0.5+0j, 0.5+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j ], 'F').reshape(16, 1)).all(), "test_08b Failed"
def test_08c():
    assert (inc(5) == np.array([ 0.5+0j, 0.5+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j ], 'F').reshape(32, 1)).all(), "test_08c Failed"