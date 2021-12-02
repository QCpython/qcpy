"""
QuantumCircuit.py

Sources:
https://en.wikipedia.org/wiki/Quantum_logic_gate
"""
from Qubit import Qubit
from .Graph import *
import numpy as np
import math

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
        # pull out qubit at bit position in self._qubit_array[bit]

        # multiply the NOT gate against the qubit.state array

        # put result of that product back in to the self._qubit_array[bit]
        pass
    def y(self, bit: int):
        """
        Params:
            bit (int): the nth-bit position on circuit.
        Returns:
            None
        """
        # pull out qubit at bit position in self._qubit_array[bit]

        # multiply the Y gate against the qubit.state array

        # put result of that product back in to the self._qubit_array[bit]
        pass
    def z(self, bit: int):
        """
        Z-Gate Operation on specifid qubit.
        Params:
            bit (int): the nth-bit position on circuit.
        Returns:
            None
        """
        # pull out qubit at bit position in self._qubit_array[bit]

        # multiply the Z gate against the qubit.state array

        # put result of that product back in to the self._qubit_array[bit]
        pass
    def hadamard(self, bit: int):
        """
        Hadamard-Gate Operation on specifid qubit.
        Params:
            bit (int): the nth-bit position on circuit.
        Returns:
            None
        """
        # pull out qubit at bit position in self._qubit_array[bit]

        # multiply the Hadamard gate against the qubit.state array

        # put result of that product back in to the self._qubit_array[bit]
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
        q = self._qubit_array.copy() # make a copy of self._qubit_array which will be used as a queue
        if len(q) > 1: # tensor only if the length of self._qubit_array is greater than 1
            final_matrix = np.kron(q[0], q[1]) # create our final_matrix
            # use numpy's Kronecker product on the first 2 qubit states and then delete them from the queue
            del q[0]
            del q[0]
            while q: # go through the rest of the queue
                final_matrix = np.kron(final_matrix, q[0])
                del q[0]
        # square all of the values in matrix to get probabilties of each qubit state
        probability_matrix = np.square(final_matrix)
        return(probability_matrix)
    def graph(self):
        """
        Generate a graph using probabilities().
        Params:
            None
        Returns:
            png file.
        """
        pass