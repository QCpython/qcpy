from QCpy.QuantumGate import Identity
import numpy as np


def test_qg_01():
    assert (
        Identity().matrix == np.array([
            [1 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j]
        ], 'F')
    ).all(), 'test_qg_01 Failed on Identity'
