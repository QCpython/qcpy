from QCpy.QuantumGate import S
import numpy as np


def test_qg_10():
    assert (
        S().matrix == np.array([
            [1 + 0j, 0 + 0j],
            [0 + 0j, 0 + 1j]
        ], 'F')
    ).all(), 'test_qg_10 Failed on S'
