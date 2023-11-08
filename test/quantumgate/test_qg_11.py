import numpy as np

from qcpy.quantumgate import sdg


def test_qg_11():
    assert (sdg() == np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 - 1j]], "F")).all(), "test_qg_11 Failed on Sdg"
