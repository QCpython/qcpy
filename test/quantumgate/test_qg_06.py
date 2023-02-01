from QCpy.QuantumGate import CNot
import numpy as np


def test_qg_06a():
    assert (CNot(inverse=False).matrix == np.array([
        [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
        [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
        [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j]
    ], 'F')).all(), 'test_qg_06a Failed'


def test_qg_06b():
    assert (CNot(inverse=True).matrix == np.array([
        [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
        [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j]
    ], 'F')).all(), 'test_qg_06b Failed'
