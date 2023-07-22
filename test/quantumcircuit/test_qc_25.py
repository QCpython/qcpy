"""
QMACE Testing - 05

"""

from QCpy import QuantumCircuit
from QCpy.Core import qmace

def inc(x):
    qc = QuantumCircuit(qubits = x, prep = 'z')
    qc.hadamard(x - 1)
    qc.cnot(x - 1, 0)
    return qc.state()

def inc_2(x):
    qc = qmace.QuantumCircuit(qubits = x, prep = 'z')
    qc.hadamard(x - 1)
    qc.cnot(x - 1, 0)
    return qc.execute().state()


def test_25a():
    assert (inc(2) == inc_2(2)).all(), "test_25a Failed"

def test_25b():
    assert (inc(3) == inc_2(3)).all(), "test_25b Failed"

def test_25c():
    assert (inc(4) == inc_2(4)).all(), "test_25c Failed"

def test_25d():
    assert (inc(5) == inc_2(5)).all(),"test_25d Failed"

