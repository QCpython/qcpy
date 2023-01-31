from QCpy import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    return qc.state()

def test_01a():
    assert (inc(1) == np.array([ 1+0j, 0+0j], 'F').reshape(2, 1)).all(), "test_01a Failed"
def test_01b():
    assert (inc(2) == np.array([ 1+0j, 0+0j, 0+0j, 0+0j], 'F').reshape(4, 1)).all(), "test_01b Failed"
def test_01c():
    assert (inc(3) == np.array([ 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j ]).reshape(8, 1)).all(), "test_01c Failed"
def test_01d():
    assert (inc(4) == np.array([ 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j], 'F').reshape(16, 1)).all(), "test_01d Failed"