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
        bits = bit_str.split()
        for bit in bits:
            qb = Qubit(int(bit))
            self._qubit_array.append(qb)

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
    def measure(self):
        """
        Collapses circuit into one state.
        Params:
            None
        Returns:
            final_matrix (list): collapse matrix.
        """
        # get probabilities matrix from self.probabilities()
        
        # get final matrix based off randomizer using each value in probabilities matrix as weights
        pass
    def probalities(self):
        """
        Returns matrix with all probabilities for each state.
        Params:
            None
        Returns:
            probability_matrix (list): matrix with all weighted probabilities.
        """
        # tensor all of the qubits in self._qubit_array together to get a final matrix

        # square all of the values in matrix to get probabilties of each qubit state
        pass
    def graph(self):
        """
        Generate a graph using probabilities().
        Params:
            None
        Returns:
            png file.
        """
        pass