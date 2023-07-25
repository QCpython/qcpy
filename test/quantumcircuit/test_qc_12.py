from qcpy import quantumcircuit
import numpy as np


def inc(x):
    qc = quantumcircuit(qubits=x, little_endian=True, prep='z')
    qc.h(0)
    qc.swap(0, x - 1)
    return qc.flatten()


def test_12a():
    assert (
        inc(2) == np.array([
            0.707 + 0j, 0 + 0j, 0.707 + 0j, 0 + 0j
        ], 'F')
    ).all(), "test_12a Failed on hadamard -> swap"


def test_12b():
    assert (
        inc(3) == np.array([
            0.707 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0.707 + 0j, 0 + 0j, 0 + 0j, 0 + 0j
        ], 'F')
    ).all(), "test_12b Failed on hadamard -> swap"


def test_12c():
    assert (
        inc(4) == np.array([
            0.707 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0.707 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j
        ], 'F')
    ).all(), "test_12c Failed on hadamard -> swap"
