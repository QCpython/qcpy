import numpy as np

from qcpy.quantumgate import sx


def test_qg_17():
    assert (sx() == np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]], "F") * (1 / 2)).all(), "test_qg_17 Failed on Sx"
