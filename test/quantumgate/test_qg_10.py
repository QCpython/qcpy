from qcpy.quantumgate import s
import numpy as np


def test_qg_10():
    assert (
        s() == np.array([
            [1 + 0j, 0 + 0j],
            [0 + 0j, 0 + 1j]
        ], 'F')
    ).all(), 'test_qg_10 Failed on S'
