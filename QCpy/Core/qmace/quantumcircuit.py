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
    
    def identity(self, qubit: int):
        self._qmace_matrix.identity(qubit)

    def x(self, qubit: int):
        self._qmace_matrix.x(qubit)

    def y(self, qubit: int):
        self._qmace_matrix.y(qubit)

    def z(self, qubit: int):
        self._qmace_matrix.z(qubit)

    def hadamard(self, qubit: int):
        self._qmace_matrix.hadamard(qubit)

    def phase(self, qubit: int, theta: float = np.pi / 2):
        self._qmace_matrix.phase(qubit, theta)

    def s(self, qubit: int):
        self._qmace_matrix.s(qubit)

    def sdg(self, qubit: int):
        self._qmace_matrix.sxdg(qubit)

    def t(self, qubit: int):
        self._qmace_matrix.t(qubit)

    def tdg(self, qubit: int):
        self._qmace_matrix.tdg(qubit)

    def rz(self, qubit: int, theta: float = np.pi / 2):
        self._qmace_matrix.rz(qubit, theta)

    def rx(self, qubit: int, theta: float = np.pi / 2):
        self._qmace_matrix.rx(qubit, theta)

    def ry(self, qubit: int, theta: float = np.pi / 2):
        self._qmace_matrix.ry(qubit, theta)

    def sx(self, qubit: int):
        self._qmace_matrix.sx(qubit)

    def sxdg(self, qubit: int):
        self._qmace_matrix.sxdg(qubit)

    def u(self, qubit: int, theta: float = np.pi / 2, phi: float = np.pi / 2, lmbda: float = np.pi / 2):
        self._qmace_matrix.u(qubit, theta, phi, lmbda)
    
    
