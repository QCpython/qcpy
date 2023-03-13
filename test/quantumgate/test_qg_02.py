from QCpy.QuantumGate import PauliX
import numpy as np


def test_qg_02():
    assert (
        PauliX().matrix == np.array([
            [0 + 0j, 1 + 0j],
            [1 + 0j, 0 + 0j]
        ], 'F')
    ).all(), 'test_qg_02 Failed on PauliX'
