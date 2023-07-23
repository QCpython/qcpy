import numpy as np
from .qmace import Qmace
from .controlledkronecker import ControlledKronecker
from ...quantumgate import *

class QuantumCircuit:
    def __init__(self, qubits: int, little_endian: bool = False, prep: chr = 'z'):
        self._little_endian = little_endian
        self._circuit_size = qubits
        self._qmace_matrix = Qmace(self._circuit_size, self._little_endian, prep)

    def setQubit(self, qubit: int, prep: chr = 'z'):
        self._qmace_matrix.set_qubit(qubit, prep)

    def execute(self):
        return ControlledKronecker(self._qmace_matrix)
    
    def identity(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, Identity().matrix)

    def x(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, PauliX().matrix)

    def y(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, PauliY().matrix)

    def z(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, PauliZ().matrix)

    def hadamard(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, Hadamard().matrix)

    def phase(self, qubit: int, theta: float = np.pi / 2):
        self._qmace_matrix.merge_single_gate(qubit, Phase(theta).matrix)

    def s(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, S().matrix)

    def sdg(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, Sdg().matrix)

    def t(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, T().matrix)

    def tdg(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, Tdg().matrix)

    def rz(self, qubit: int, theta: float = np.pi / 2):
        self._qmace_matrix.merge_single_gate(qubit, Rz(theta).matrix)

    def rx(self, qubit: int, theta: float = np.pi / 2):
        self._qmace_matrix.merge_single_gate(qubit, Rx(theta).matrix)

    def ry(self, qubit: int, theta: float = np.pi / 2):
        self._qmace_matrix.merge_single_gate(qubit, Ry(theta).matrix)

    def sx(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, Sx().matrix)

    def sxdg(self, qubit: int):
        self._qmace_matrix.merge_single_gate(qubit, Sxdg().matrix)

    def u(self, qubit: int, theta: float = np.pi / 2, phi: float = np.pi / 2, lmbda: float = np.pi / 2):
        self._qmace_matrix.merge_single_gate(qubit, U(theta, phi, lmbda).matrix)

    def cnot(self, control_qubit: int, target_qubit: int):
        inverse = False

        if control_qubit > target_qubit:

            inverse = True
            control_qubit, target_qubit = target_qubit, control_qubit
            
            self._qmace_matrix.merge_single_gate(control_qubit, 
                                                 Hadamard().matrix)
            self._qmace_matrix.merge_single_gate(target_qubit, 
                                                 Hadamard().matrix)

        self._qmace_matrix.merge_controlled_gate(control_qubit, 
                                                 target_qubit, 
                                                 PauliX().matrix)
        if inverse:

            self._qmace_matrix.merge_single_gate(control_qubit, Hadamard().matrix)
            self._qmace_matrix.merge_single_gate(target_qubit, Hadamard().matrix)
        return
    
    def swap(self, control_qubit: int, target_qubit: int):

        self.cnot(target_qubit, control_qubit)

        self.cnot(control_qubit, target_qubit)

        self.cnot(target_qubit, control_qubit)

        return

    def get_all(self):
        self._qmace_matrix.get_all()
    
    
