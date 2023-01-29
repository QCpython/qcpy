from QCpy.QuantumGate import PauliY
import numpy as np

def test_qg_03():
    assert(PauliY().matrix == np.array([
            [0+0j, 0-1j],
            [0+1j, 0+0j]
        ], 'F')).all(), 'test_qg_03 Failed'