"""
QMACE Testing - 06

"""

from QCpy import QuantumCircuit
from QCpy.Core import qmace

def inc(x):
    qc = QuantumCircuit(qubits = x, prep = 'z')
    qc.hadamard(0)
    qc.cnot(0, x - 1)
    qc.hadamard(0)
    return qc.state()

def inc_2(x):
    qc = qmace.QuantumCircuit(qubits = x, prep = 'z')
    qc.hadamard(0)
    qc.cnot(0, x - 1)
    qc.hadamard(0)
    return qc.execute().state()


def test_26a():
    assert (inc(2) == inc_2(2)).all(), "test_26a Failed"

def test_26b():
    assert (inc(3) == inc_2(3)).all(), "test_26b Failed"

def test_26c():
    assert (inc(4) == inc_2(4)).all(), "test_26c Failed"

def test_26d():
    assert (inc(5) == inc_2(5)).all(),"test_26d Failed"

