from QuantumCircuit import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    qc.hadamard(x - 2)
    qc.hadamard(x - 1)
    qc.rccx(x - 1, x - 2, 0)
    return qc.state()

def test_15a():
    assert (inc(3) == np.array([ 0.5+0j, 0+0j, 0.5+0j, 0+0j, 0.5+0j, 0+0j, 0+0j, 0+0.5j ]).reshape(8, 1)).all(), "test_15a Failed"
def test_15b():
    assert (inc(4) == np.array([ 0.5+0j, 0+0j, 0+0j, 0+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0.5j, 0+0j, 0+0j ]).reshape(16, 1)).all(), "test_15b Failed"
def test_15c():
    assert (inc(5) == np.array([ 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0.5j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j ]).reshape(32, 1)).all(), "test_15c Failed"
