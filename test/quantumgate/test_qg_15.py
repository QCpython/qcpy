from qcpy.quantumgate import rx
import numpy as np


def test_qg_15():
    assert (
        rx() == np.array([
            [np.cos((np.pi / 2) / 2), 0 - 1j * np.sin((np.pi / 2) / 2)],
            [0 - 1j * np.sin((np.pi / 2) / 2), np.cos((np.pi / 2) / 2)]
        ], 'F')
    ).all(), 'test_qg_15 Failed on Rx'
