from QCpy import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    for i in range(x):
        qc.hadamard(i)  
    for i in range(x):
        qc.tdg(i)
    return qc.state()

def test_10a():
    assert (inc(1) == np.array([ 0.707+0j, 0.5-0.5j ], 'F').reshape(2, 1)).all(), "test_10a Failed"
def test_10b():
    assert (inc(2) == np.array([ 0.5+0j, 0.354-0.354j, 0.354-0.354j, 0-0.5j ], 'F').reshape(4, 1)).all(), "test_10b Failed"
def test_10c():
    assert (inc(3) == np.array([ 0.354+0j, 0.25-0.25j, 0.25-0.25j, 0-0.354j, 0.25-0.25j, 0-0.354j, 0-0.354j, -0.25-0.25j ], 'F').reshape(8, 1)).all(), "test_10c Failed"
def test_10d():
    assert (inc(4) == np.array([ 0.25+0j, 0.177-0.177j, 0.177-0.177j, 0-0.25j, 0.177-0.177j, 0-0.25j, 0-0.25j, -0.177-0.177j, 0.177-0.177j, 0-0.25j, 0-0.25j, -0.177-0.177j, 0-0.25j, -0.177-0.177j, -0.177-0.177j, -0.25+0j ], 'F').reshape(16, 1)).all(), "test_10d Failed"