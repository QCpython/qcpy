from qcpy import quantumcircuit
import numpy as np


def inc(x):
    qc = quantumcircuit(qubits=x, little_endian=True, prep='z')
    qc.hadamard(x - 1)
    qc.hadamard(0)
    qc.toffoli(x - 1, 0, x - 2)
    return qc.state()


def test_11a():
    assert (
        inc(3) == np.array([
            0.5 + 0j, 0.5 + 0j, 0 + 0j, 0 + 0j,
            0.5 + 0j, 0 + 0j, 0 + 0j, 0.5 + 0j
        ], 'F').reshape(8, 1)
    ).all(), "test_11a Failed on hadamard -> hadamard -> toffoli"


def test_11b():
    assert (
        inc(4) == np.array([
            0.5 + 0j, 0.5 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0.5 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0.5 + 0j, 0 + 0j, 0 + 0j
        ], 'F').reshape(16, 1)
    ).all(), "test_11b Failed on hadamard -> hadamard -> toffoli"


def test_11c():
    assert (
        inc(5) == np.array([
            0.5 + 0j, 0.5 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0.5 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0.5 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j
        ], 'F').reshape(32, 1)
    ).all(), "test_11c Failed on hadamard -> hadamard -> toffoli"
