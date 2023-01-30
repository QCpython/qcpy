from QCpy.QuantumGate import T
import numpy as np

def test_qg_12():
    assert(T().matrix == np.array([
            [1+0j, 0+0j],
            [0+0j, np.exp((0+1j * np.pi) / 4)]
        ], 'F')).all(), 'test_qg_12 Failed'