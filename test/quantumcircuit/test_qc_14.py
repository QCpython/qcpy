from qcpy import quantumcircuit
import numpy as np


def inc(x):
    qc = quantumcircuit(qubits=x, little_endian=True, prep='z')
    qc.h(0)
    qc.h(1)
    qc.rccx(0, 1, x - 1)
    return qc.flatten()


def test_11a():
    assert (
        inc(3) == np.array([
            0.5 + 0j, 0.5 + 0j, 0.5 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0.5j
        ], 'F')
    ).all(), "test_11a Failed on hadamard -> hadamard -> rccx"


def test_11b():
    assert (
        inc(4) == np.array([
            0.5 + 0j, 0.5 + 0j, 0.5 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0.5j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j
        ], 'F')
    ).all(), "test_11b Failed on hadamard -> hadamard -> rccx"


def test_11c():
    assert (
        inc(5) == np.array([
            0.5 + 0j, 0.5 + 0j, 0.5 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0.5j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j
        ], 'F')
    ).all(), "test_11c Failed on hadamard -> hadamard -> rccx"
