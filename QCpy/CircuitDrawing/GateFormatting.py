from ..QuantumGate import *
import sys

class GateFormatting:
    def __init__(self):
        self._single_gates = []
        self._multi_gates = []
        current_module = sys.modules[__name__]
        for key in dir(current_module):
            if isinstance( getattr(current_module, key), type) and key != 'GateFormatting':
                gate_to_implement = getattr(sys.modules[__name__], key)()
                if  gate_to_implement.matrix.shape == (2,2):
                    self._single_gates.append(gate_to_implement._symbol)
                else:
                    self._multi_gates.append(gate_to_implement._symbol)
