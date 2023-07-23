from qcpy.quantumgate import ry
import numpy as np


def test_qg_16():
    assert (
        ry() == np.array([
            [np.cos((np.pi / 2) / 2), -1 * np.sin((np.pi / 2) / 2)],
            [np.sin((np.pi / 2) / 2), np.cos((np.pi / 2) / 2)]
        ], 'F')
    ).all(), 'test_qg_16 Failed on Ry'
