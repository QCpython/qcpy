"""
QMACE Testing - 02

"""

from QCpy import QuantumCircuit
from QCpy.Core import qmace

def inc(x):
    qc = QuantumCircuit(qubits = x, prep = 'z')
    for i in range(x):
        qc.hadamard(i)
    return qc.state()

def inc_2(x):
    qc = qmace.QuantumCircuit(qubits = x, prep = 'z')
    for i in range(x):
        qc.hadamard(i)
    return qc.execute().state()


def test_22a():
    assert (inc(1) == inc_2(1)).all(), "test_22a Failed"

def test_22b():
    assert (inc(2) == inc_2(2)).all(), "test_22b Failed"

def test_22c():
    assert (inc(3) == inc_2(3)).all(), "test_22c Failed"

def test_22d():
    assert (inc(4) == inc_2(4)).all(),"test_22d Failed"