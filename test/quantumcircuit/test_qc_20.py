from QCpy import QuantumCircuit
import numpy as np


def inc(x):
    qc = QuantumCircuit(qubits=x, little_endian=True, prep='z')
    qc.hadamard(x - 1)
    qc.rzz(x - 1, 0)
    qc.hadamard(x - 1)
    return qc.state()


def test_20a():
    assert (
        inc(2) == np.array([
            0.707 + 0j, 0 + 0j, 0 - 0.707j, 0 + 0j
        ], 'F').reshape(4, 1)
    ).all(), "test_20a Failed on hadamard -> rzz -> hadamard"


def test_20b():
    assert (
        inc(3) == np.array([
            0.707 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 - 0.707j, 0 + 0j, 0 + 0j, 0 + 0j
        ], 'F').reshape(8, 1)
    ).all(), "test_20b Failed on hadamard -> rzz -> hadamard"


def test_20c():
    assert (
        inc(4) == np.array([
            0.707 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 - 0.707j, 0 + 0j, 0 + 0j, 0 + 0j,
            0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j
        ], 'F').reshape(16, 1)
    ).all(), "test_20c Failed on hadamard -> rzz -> hadamard"
