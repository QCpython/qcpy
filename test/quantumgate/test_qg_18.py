from QCpy.QuantumGate import Sxdg
import numpy as np


def test_qg_18():
    assert (Sxdg().matrix == np.array([
        [1 - 1j, 1 + 1j],
        [1 + 1j, 1 - 1j]], 'F') * (1 / 2)).all(), 'test_qg_18 Failed'
