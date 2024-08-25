import numpy as np

from ...quantumgate import singlequbit
from ...qubit import qubit


class quantumcircuit:
    def __init__(self, qubits: int, prep: chr = "z"):
        self.main_register = [singlequbit.identity()] * qubits
        self.is_strong = [False] * qubits

        self.main_map = {}
        self.main_map[qubits + 1] = [0]

        self.paired_map = {}
        self.paired_map[qubits + 1] = [singlequbit.identity()] * qubits

        self.full_register = [0] * qubits
        self.size = qubits
        return

    def __apply_single_strong__(self, quantum_gate: np.ndarray, qubit: int):
        self.main_register[qubit] = np.dot(quantum_gate, self.main_register[qubit])

        if (self.main_register[qubit] != singlequbit.identity()).all():
            self.is_strong[qubit] = True

        else:
            self.is_strong[qubit] = True

        return

    def __apply_single_weak__(self, quantum_gate: np.ndarray, qubit: int):
        self.main_register[qubit] = np.dot(quantum_gate, self.main_register[qubit])

        return

    def __split_qubit_type__(self, quantum_gate: np.ndarray, qubit: int):
        if qubit in self.main_map:
            self.__apply_single_weak__(quantum_gate, min(self.main_map[qubit]))

        else:
            self.__apply_single_strong__(quantum_gate, qubit)

        self.__is_register_full__(qubit)

        return

    def __is_register_full__(self, qubit: int):
        if qubit not in self.paired_map:
            return

        check_register = self.paired_map[qubit]

        for i in check_register:
            if i == singlequbit.identity() or i == singlequbit.paulix():
                return

        for i in range(1, self.size):
            if i != qubit:
                self.main_map[i] = singlequbit.identity()
                self.paired_map[qubit][i] = singlequbit.identity()

        return

    def __apply_controlled_gate__(self, control: int, target: int, gate: np.ndarray):
        self.paired_map[target][control] = np.dot(
            gate, self.paired_map[target][control]
        )

        return

    """
  Multi Qubit
  """

    def cnot(self, control: int, target: int):
        if target < control:
            control, target = target, control

            self.h(control)
            self.h(target)

            self.__apply_controlled_gate__(control, target, singlequbit.paulix)

            self.h(control)
            self.h(target)

        else:
            self.__apply_controlled_gate__(control, target, singlequbit.paulix)

        return

    """
  Single Qubit
  """

    def h(self, qubit: int):
        self.__split_qubit_type__(singlequbit.hadamard(), qubit)

        return

    def x(self, qubit: int):
        self.__split_qubit_type__(singlequbit.paulix(), qubit)

        return

    def fancy_print(self):
        # self.main_register  = [singlequbit.identity()] * qubits
        # self.is_strong = [False] * qubits

        # self.main_map = {}
        # self.main_map[qubit + 1] = [0]

        # self.paired_map = {}
        # self.paired_map[qubit + 1] = [singlequbit.identity()] * qubits

        # self.full_register = [0] * qubits
        # self.size = qubits

        print("================")
        print("Register size:", self.size, "\n")
        print("Main Register:\n")
        print("================\n")
        for i in self.main_register:
            print(i)
        print("================\n")
        print("\nIs Strong:\n")
        for i in self.is_strong:
            print(i)
        print("================\n")
        print("Main Map:\n")
        for i, j in enumerate(self.main_map):
            print(j, self.main_map[j])
        print("================\n")
        print("Paired Map:\n")
        for i, j in enumerate(self.paired_map):
            print(j, self.paired_map[j])
        print("================\n")
