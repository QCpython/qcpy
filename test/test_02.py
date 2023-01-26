from QCpy import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    for i in range(x):
        qc.hadamard(i)  
    return qc.state()

def test_02a():
    assert (inc(1) == np.array([ 0.707+0j, 0.707+0j ]).reshape(2, 1)).all(), "test_02a Failed"
def test_02b():
    assert (inc(2) == np.array([ 0.5+0j, 0.5+0j, 0.5+0j, 0.5+0j ]).reshape(4, 1)).all(), "test_02b Failed"
def test_02c():
    assert (inc(3) == np.array([ 0.354+0j, 0.354+0j, 0.354+0j, 0.354+0j, 0.354+0j, 0.354+0j, 0.354+0j, 0.354+0j ]).reshape(8, 1)).all(), "test_02c Failed"
def test_02d():
    assert (inc(4)== np.array([ 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j, 0.25+0j ]).reshape(16, 1)).all(), "test_02d Failed"