from ...qubit import *
from ..tools import *
import numpy as np
from .qmace import Qmace

class QuantumCircuit:
    def __init__(self, qubits: int, little_endian: bool = False, prep: chr = 'z'):
        self._little_endian = little_endian
        self._circuit_size = qubits
        self._state = [Qubit(prep).state for _ in range (self._circuit_size)]
        self._qmace_matrix = Qmace(self._circuit_size, self._little_endian)

    def setQubit(self, qubit: int, prep: chr = 'z'):
        self._state[qubit] = Qubit(prep).state

    def execute(self):
        return self._qmace_matrix.execute(self._state)
    
    
