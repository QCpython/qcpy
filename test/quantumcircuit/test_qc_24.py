"""
QMACE Testing - 04

"""

from QCpy import QuantumCircuit
from QCpy.Core import qmace

def inc(x):
    qc = QuantumCircuit(qubits = x, prep = 'z')
    qc.hadamard(0)
    qc.cnot(0,x - 1)
    return qc.state()

def inc_2(x):
    qc = qmace.QuantumCircuit(qubits = x, prep = 'z')
    qc.hadamard(0)
    qc.cnot(0,x - 1)
    return qc.execute().state()


def test_24a():
    assert (inc(2) == inc_2(2)).all(), "test_24a Failed"

def test_24b():
    assert (inc(3) == inc_2(3)).all(), "test_24b Failed"

def test_24c():
    assert (inc(4) == inc_2(4)).all(), "test_24c Failed"

def test_24d():
    assert (inc(5) == inc_2(5)).all(),"test_24d Failed"