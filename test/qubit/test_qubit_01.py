from qcpy import Qubit
import numpy as np


def test_qubit_01a():
    assert (
        Qubit() == np.array([[1+0j, 0+0j]], 'F').reshape(2, 1)
    ).all(), 'test_qubit_01a Failed on Qubit'
