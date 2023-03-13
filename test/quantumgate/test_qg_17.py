from QCpy.QuantumGate import Sx
import numpy as np


def test_qg_17():
    assert (
        Sx().matrix == np.array([
            [1 + 1j, 1 - 1j],
            [1 - 1j, 1 + 1j]], 'F') * (1 / 2)
    ).all(), 'test_qg_17 Failed on Sx'
