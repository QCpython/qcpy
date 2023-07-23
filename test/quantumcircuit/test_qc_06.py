from qcpy import quantumcircuit
import numpy as np


def inc(x):
    qc = quantumcircuit(qubits=x, little_endian=True, prep='z')
    qc.hadamard(0)
    qc.cnot(0, x - 1)
    qc.hadamard(0)
    return qc.state()


def test_06a():
    assert (
        inc(2) == np.array([
            0.5 + 0j, 0.5 + 0j, 0.5 + 0j, -0.5 + 0j
        ], 'F').reshape(4, 1)
    ).all(), "test_06a Failed on hadamard -> cnot -> hadamard"


def test_06b():
    assert (
        inc(3) == np.array([
            0.5 + 0j, 0.5 + 0j, 0 + 0j, 0 + 0j,
            0.5 + 0j, -0.5 + 0j, 0 + 0j, 0 + 0j
        ], 'F').reshape(8, 1)
    ).all(), "test_06b Failed on hadamard -> cnot -> hadamard"


def test_06c():
    assert (
        inc(4) == np.array([
            0.5 + 0j, 0.5 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0.5 + 0j, -0.5 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j
        ], 'F').reshape(16, 1)
    ).all(), "test_06c Failed on hadamard -> cnot -> hadamard"
