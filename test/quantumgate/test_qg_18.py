from qcpy.quantumgate import sxdg
import numpy as np


def test_qg_18():
    assert (
        sxdg() == np.array([
            [1 - 1j, 1 + 1j],
            [1 + 1j, 1 - 1j]], 'F') * (1 / 2)
    ).all(), 'test_qg_18 Failed on Sxdg'
