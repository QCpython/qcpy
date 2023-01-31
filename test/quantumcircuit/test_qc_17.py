from QCpy import QuantumCircuit
import numpy as np


def inc(x):
    qc = QuantumCircuit(qubits=x, little_endian=True, prep='z')
    qc.hadamard(0)
    qc.hadamard(1)
    qc.hadamard(2)
    qc.rc3x(0, 1, 2, x - 1)
    return qc.state()


def test_17a():
    assert (inc(4) == np.array([0.354 +
                                0j, 0.354 +
                                0j, 0.354 +
                                0j, 0 +
                                0.354j, 0.354 +
                                0j, 0.354 +
                                0j, 0.354 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, -
                                0.354 +
                                0j], 'F').reshape(16, 1)).all(), "test_17a Failed"


def test_17b():
    assert (inc(5) == np.array([0.354 +
                                0j, 0.354 +
                                0j, 0.354 +
                                0j, 0 +
                                0.354j, 0.354 +
                                0j, 0.354 +
                                0j, 0.354 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, -
                                0.354 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j, 0 +
                                0j], 'F').reshape(32, 1)).all(), "test_17b Failed"
