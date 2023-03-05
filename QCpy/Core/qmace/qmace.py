from ...QuantumGate import *
from ..tools import *
import numpy as np


class Qmace:
    def __init__(self, qubits: int, little_endian: bool = False):
        self._little_endian = little_endian
        self._circuit_size = qubits
        self._order_of_operation = np.array(
            [[1] for _ in range(self._circuit_size)])

    def __merge_single_gate__(self, qubit: int, single_qubit_gate: np.array):
        if (self._order_of_operation[qubit]

                [len(self._order_of_operation)] == 1):
            self._order_of_operation[qubit][len(
                self._order_of_operation)] = single_qubit_gate
        else:

            self._order_of_operation[qubit][len(self._order_of_operation)] = np.dot(
                self._order_of_operation[qubit][len(self._order_of_operation)], single_qubit_gate)
        return

    def execute(self, state):

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
