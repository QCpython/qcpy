"""
QMACE Testing - 07

"""

from QCpy import QuantumCircuit
from QCpy.Core import qmace

def inc(x):
    qc = QuantumCircuit(qubits = x, prep = 'z')
    qc.hadamard(x - 1)
    qc.cnot(x - 1, 0)
    qc.hadamard(x - 1)
    return qc.state()

def inc_2(x):
    qc = qmace.QuantumCircuit(qubits = x, prep = 'z')
    qc.hadamard(x - 1)
    qc.cnot(x - 1, 0)
    qc.hadamard(x - 1)
    return qc.execute().state()


def test_27a():
    assert (inc(2) == inc_2(2)).all(), "test_27a Failed"

def test_27b():
    assert (inc(3) == inc_2(3)).all(), "test_27b Failed"

def test_27c():
    assert (inc(4) == inc_2(4)).all(), "test_27c Failed"

def test_27d():
    assert (inc(5) == inc_2(5)).all(),"test_27d Failed"

