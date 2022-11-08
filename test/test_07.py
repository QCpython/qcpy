from QuantumCircuit import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    qc.hadamard(x - 1)
    qc.cnot(x - 1, 0)
    qc.hadamard(x - 1)
    return qc.state()

def test_07a():
    assert (inc(2) == np.array([ 0.5+0j, 0.5+0j, 0.5+0j, -0.5+0j ]).reshape(4, 1)).all(), "test_07a Failed"
def test_07b():
    assert (inc(3) == np.array([ 0.5+0j, 0.5+0j, 0+0j, 0+0j, 0.5+0j, -0.5+0j, 0+0j, 0+0j ]).reshape(8, 1)).all(), "test_07b Failed"
def test_07c():
    assert (inc(4) == np.array([ 0.5+0j, 0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0.5+0j, -0.5+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j ]).reshape(16, 1)).all(), "test_07c Failed"