"""
QMACE Testing - 01

"""

from QCpy import QuantumCircuit
from QCpy.Core import qmace

def inc(x):
    qc = QuantumCircuit(qubits = x, prep = 'z')
    return qc.state()

def inc_2(x):
    qc = qmace.QuantumCircuit(qubits = x, prep = 'z')
    return qc.execute().state()


def test_21a():
    assert (inc(1) == inc_2(1)).all(), "test_21a Failed"

def test_21b():
    assert (inc(2) == inc_2(2)).all(), "test_21b Failed"

def test_21c():
    assert (inc(3) == inc_2(3)).all(), "test_21c Failed"

def test_21d():
    assert (inc(4) == inc_2(4)).all(),"test_21d Failed"