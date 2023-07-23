"""
QMACE Testing - 03

"""

from QCpy import QuantumCircuit
from QCpy.Core import qmace

def inc(x):
    qc = QuantumCircuit(qubits = x, prep = 'z')
    for i in range(x):
        qc.hadamard(i)
    for i in range(x):
        qc.t(i)
    return qc.state()

def inc_2(x):
    qc = qmace.QuantumCircuit(qubits = x, prep = 'z')
    for i in range(x):
        qc.hadamard(i)
    for i in range(x):
        qc.t(i)
    return qc.execute().state()


def test_23a():
    assert (inc(1) == inc_2(1)).all(), "test_23a Failed"

def test_23b():
    assert (inc(2) == inc_2(2)).all(), "test_23b Failed"

def test_23c():
    assert (inc(3) == inc_2(3)).all(), "test_23c Failed"

def test_23d():
    assert (inc(4) == inc_2(4)).all(),"test_23d Failed"