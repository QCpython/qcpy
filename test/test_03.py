from QuantumCircuit import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    for i in range(x):
        qc.hadamard(i)  
    for i in range(x):
        qc.t(i)
    return qc.state()

def test_03a():
    assert (inc(1) == np.array([ 0.707+0j, 0.5+0.5j ]).reshape(2, 1)).all(), "test_01a Failed"
def test_03b():
    assert inc(2).all() == np.array([ 0.5+0j, 0.354+0.354j, 0.354+0.354j, 0+0.5j ]).reshape(4, 1).all(), "test_01b Failed"
def test_03c():
    assert inc(3).all() == np.array([ 0.354+0j, 0.25+0.25j, 0.25+0.25j, 0+0.354j, 0.25+0.25j, 0+0.354j, 0+0.354j, -0.25+0.25j ]).reshape(8, 1).all(), "test_01c Failed"
def test_03d():
    assert inc(4).all() == np.array([ 0.25+0j, 0.177+0.177j, 0.177+0.177j, 0+0.25j, 0.177+0.177j, 0+0.25j, 0+0.25j, -0.177+0.177j, 0.177+0.177j, 0+0.25j, 0+0.25j, -0.177+0.177j, 0+0.25j, -0.177+0.177j, -0.177+0.177j, -0.25+0j ]).reshape(16, 1).all(), "test_01d Failed"