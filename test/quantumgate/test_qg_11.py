from QCpy.QuantumGate import Sdg
import numpy as np


def test_qg_11():
    assert (
        Sdg().matrix == np.array([
            [1 + 0j, 0 + 0j],
            [0 + 0j, 0 - 1j]
        ], 'F')
    ).all(), 'test_qg_11 Failed on Sdg'
