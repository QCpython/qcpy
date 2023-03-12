from QCpy.QuantumGate import Hadamard
import numpy as np


def test_qg_05():
    assert (
        Hadamard().matrix == np.array([
            [1 + 0j, 1 + 0j],
            [1 + 0j, -1 + 0j]
        ], 'F') * (1 / np.sqrt(2))
    ).all(), 'test_qg_05 Failed on Hadamard'
