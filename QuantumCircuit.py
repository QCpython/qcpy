"""
QuantumCircuit.py

Sources:
https://en.wikipedia.org/wiki/Quantum_logic_gate
"""
from Qubit import Qubit
from .LinearAlg import *
from .Graph import *

class QuantumCircuit:
    def __init__(self, bit_str: str):
        self._bit_str = bit_str # string of qubits bits in system
        self._qubit_array = [] # array holding qubits
        # using bit_str, generate qubits and add to array
    def __tensor_matrices(self, m1: list, m2: list) -> list:
        """
        Tensor two matrices together and return a larger matrix.
        Params:
            m1 (list): matrix one.
            m2 (list): matrix two.
        Returns:
            final_matrix (list): tensor product of m1 (x) m2.
        """
        pass
    def x(self, bit: int):
        """
        X-Gate Operation on specified qubit.
        Params:
            bit (int): the nth-bit position on circuit.
        Returns:
            None
        """
        pass
    def y(self, bit: int):
        """
        Params:
            bit (int): the nth-bit position on circuit.
        Returns:
            None
        """
        pass
    def z(self, bit: int):
        """
        Z-Gate Operation on specifid qubit.
        Params:
            bit (int): the nth-bit position on circuit.
        Returns:
            None
        """
        pass
    def hadamard(self, bit: int):
        """
        Hadamard-Gate Operation on specifid qubit.
        Params:
            bit (int): the nth-bit position on circuit.
        Returns:
            None
        """
        pass
    def swap(self, bit_1: int, bit_2: int):
        """
        Swap-Gate Operation on specifid qubit.
        Params:
            bit_1 (int): the nth-bit position on circuit for swap.
            bit_2 (int): the nth-bit position on circuit for swap.
        Returns:
            None
        """
    def cnot(self, control: int, target: int):
        """
        Controlled-NOT-Gate Operation on specifid qubit.
        Params:
            bit_1 (int): the nth-bit position on circuit for swap.
            bit_2 (int): the nth-bit position on circuit for swap.
        Returns:
            None
        """
        pass
    def measure(self):
        """
        Collapses circuit into one state.
        Params:
            None
        Returns:
            final_matrix (list): collapse matrix.
        """
    def probalities(self):
        """
        Returns matrix with all probabilities for each state.
        Params:
            None
        Returns:
            probability_matrix (list): matrix with all weighted probabilities.
        """
    def graph(self):
        """
        Generate a graph using probabilities().
        Params:
            None
        Returns:
            png file.
        """
        pass