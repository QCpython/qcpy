from QCpy.QuantumGate import Swap
import numpy as np


def test_qg_07():
    assert (
        Swap().matrix == np.array([
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j]
        ], 'F')
    ).all(), 'test_qg_07 Failed on Swap'
