import numpy as np

from qcpy.quantumgate import t


def test_qg_12():
    assert (
        t() == np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp((0 + 1j * np.pi) / 4)]], "F")
    ).all(), "test_qg_12 Failed on T"
