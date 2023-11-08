import numpy as np

from qcpy import quantumcircuit


def inc(x):
    qc = quantumcircuit(qubits=x, little_endian=True, prep="z")
    qc.h(0)
    qc.rzz(0, x - 1)
    qc.h(0)
    return qc.flatten()


def test_19a():
    assert (
        inc(2) == np.array([0.707 + 0j, 0 - 0.707j, 0 + 0j, 0 + 0j], "F")
    ).all(), "test_19a Failed on hadamard -> rzz -> hadamard"


def test_19b():
    assert (
        inc(3) == np.array([0.707 + 0j, 0 - 0.707j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j], "F")
    ).all(), "test_19b Failed on hadamard -> rzz -> hadamard"


def test_19c():
    assert (
        inc(4)
        == np.array(
            [
                0.707 + 0j,
                0 - 0.707j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
            ],
            "F",
        )
    ).all(), "test_19c Failed on hadamard -> rzz -> hadamard"
