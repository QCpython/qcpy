from qcpy import quantumcircuit
import numpy as np


def inc(x):
    qc = quantumcircuit(qubits=x, little_endian=True, prep='z')
    for i in range(x):
        qc.hadamard(i)
    return qc.state()


def test_02a():
    assert (
        inc(1) == np.array([0.707 + 0j, 0.707 + 0j], 'F').reshape(2, 1)
    ).all(), "test_02a Failed on hadamard"


def test_02b():
    assert (
        inc(2) == np.array([
            0.5 + 0j, 0.5 + 0j, 0.5 + 0j, 0.5 + 0j
        ], 'F').reshape(4, 1)
    ).all(), "test_02b Failed on hadamard"


def test_02c():
    assert (
        inc(3) == np.array([
            0.354 + 0j, 0.354 + 0j, 0.354 + 0j, 0.354 + 0j,
            0.354 + 0j, 0.354 + 0j, 0.354 + 0j, 0.354 + 0j
        ], 'F').reshape(8, 1)
    ).all(), "test_02c Failed on hadamard"


def test_02d():
    assert (
        inc(4) == np.array([
            0.25 + 0j, 0.25 + 0j, 0.25 + 0j, 0.25 + 0j,
            0.25 + 0j, 0.25 + 0j, 0.25 + 0j, 0.25 + 0j,
            0.25 + 0j, 0.25 + 0j, 0.25 + 0j, 0.25 + 0j,
            0.25 + 0j, 0.25 + 0j, 0.25 + 0j, 0.25 + 0j
        ], 'F').reshape(16, 1)
    ).all(), "test_02d Failed on hadamard"
