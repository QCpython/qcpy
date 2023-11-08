import numpy as np

from qcpy.quantumgate import phase


def test_qg_09():
    assert (
        phase() == np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp(0 + 1j * (np.pi / 2))]], "F")
    ).all(), "test_qg_09 Failed on Phase"
