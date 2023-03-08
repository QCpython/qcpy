from ...QuantumGate import *
from ..tools import *
import numpy as np


class Qmace:
    def __init__(self, qubits: int, little_endian: bool = False):
        self._little_endian = little_endian
        self._circuit_size = qubits
        self._order_of_operation = [[1] for _ in range(self._circuit_size)]

    def __merge_single_gate__(self, qubit: int, single_qubit_gate: np.array):
        if (type(self._order_of_operation[qubit][0]) == int):
            self._order_of_operation[qubit][0] = single_qubit_gate
        else:
            self._order_of_operation[qubit][0] = np.dot(
                self._order_of_operation[qubit][0], single_qubit_gate)
        return
    

    def execute(self, state: np.array):
        to_end_qubits = 0

        while to_end_qubits < self._circuit_size:
            if (type(self._order_of_operation[to_end_qubits][0]) != int):
                state[to_end_qubits] = np.dot(self._order_of_operation[to_end_qubits], state[to_end_qubits])
            to_end_qubits += 1

        if self._little_endian:
            curr = state[-1]
            current_len = len(state) - 2
            while current_len != -1:
                curr = np.kron(curr, state[current_len])
                current_len -= 1

        else:
            curr = state[0]
            current_len = 1

            while current_len != len(state):
                curr = np.kron(curr, state[current_len])
                current_len += 1

        return curr

    def identity(self, qubit: int):
        self.__merge_single_gate__(qubit, Identity().matrix)

    def x(self, qubit: int):
        self.__merge_single_gate__(qubit, PauliX().matrix)

    def y(self, qubit: int):
        self.__merge_single_gate__(qubit, PauliY().matrix)

    def z(self, qubit: int):
        self.__merge_single_gate__(qubit, PauliZ().matrix)

    def hadamard(self, qubit: int):
        self.__merge_single_gate__(qubit, Hadamard().matrix)

    def phase(self, qubit: int, theta: float = np.pi / 2):
        self.__merge_single_gate__(qubit, Phase(theta).matrix)

    def s(self, qubit: int):
        self.__merge_single_gate__(qubit, S().matrix)

    def sdg(self, qubit: int):
        self.__merge_single_gate__(qubit, Sdg().matrix)

    def t(self, qubit: int):
        self.__merge_single_gate__(qubit, T().matrix)

    def tdg(self, qubit: int):
        self.__merge_single_gate__(qubit, Tdg().matrix)

    def rz(self, qubit: int, theta: float = np.pi / 2):
        self.__merge_single_gate__(qubit, Rz(theta).matrix)

    def rx(self, qubit: int, theta: float = np.pi / 2):
        self.__merge_single_gate__(qubit, Rx(theta).matrix)

    def ry(self, qubit: int, theta: float = np.pi / 2):
        self.__merge_single_gate__(qubit, Ry(theta).matrix)

    def sx(self, qubit: int):
        self.__merge_single_gate__(qubit, Sx().matrix)

    def sxdg(self, qubit: int):
        self.__merge_single_gate__(qubit, Sxdg().matrix)

    def u(self, qubit: int, theta: float = np.pi / 2, phi: float = np.pi / 2, lmbda: float = np.pi / 2):
        self.__merge_single_gate__(qubit, U(theta, phi, lmbda).matrix)


