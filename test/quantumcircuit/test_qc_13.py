import numpy as np

from qcpy import quantumcircuit


def inc(x):
    qc = quantumcircuit(qubits=x, little_endian=True, prep="z")
    qc.h(0)
    qc.swap(0, x - 1)
    qc.swap(x - 1, 0)
    return qc.flatten()


def test_13a():
    assert (
        inc(2) == np.array([0.707 + 0j, 0.707 + 0j, 0 + 0j, 0 + 0j], "F")
    ).all(), "test_13a Failed on hadamard -> swap -> swap"


def test_13b():
    assert (
        inc(3) == np.array([0.707 + 0j, 0.707 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j], "F")
    ).all(), "test_13b Failed on hadamard -> swap -> swap"


def test_13c():
    assert (
        inc(4)
        == np.array(
            [
                0.707 + 0j,
                0.707 + 0j,
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
    ).all(), "test_13c Failed on hadamard -> swap -> swap"
