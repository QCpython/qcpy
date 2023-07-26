from qcpy.quantumgate import cnot
import numpy as np


def test_qg_06a():
    assert (
        cnot() == np.array([
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j]
        ], 'F')
    ).all(), 'test_qg_06b Failed on CNot'

def test_qg_06b():
    assert (
        cnot(little_endian=True) == np.array([
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j]
        ], 'F')
    ).all(), 'test_qg_06a Failed on CNot'



