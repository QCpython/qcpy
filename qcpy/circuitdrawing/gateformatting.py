import sys

from ..quantumgate import *


class GateFormatting:
    def __init__(self):
        self.single_gates = []
        self.multi_gates = []
        current_module = sys.modules[__name__]
        for key in dir(current_module):
            if isinstance(getattr(current_module, key), type) and key != "GateFormatting":
                gate_to_implement = getattr(sys.modules[__name__], key)()
                if gate_to_implement.matrix.shape == (2, 2):
                    self.single_gates.append(gate_to_implement._symbol)
                else:
                    self.multi_gates.append(gate_to_implement._symbol)
