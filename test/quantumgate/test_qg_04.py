from QCpy.QuantumGate import PauliZ
import numpy as np

def test_qg_04():
    assert(PauliZ().matrix == np.array([
            [1+0j, 0+0j],
            [0+0j, -1+0j]
        ], 'F')).all(), 'test_qg_04 Failed'