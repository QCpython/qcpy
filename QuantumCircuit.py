"""
QuantumCircuit.py

Sources:
https://en.wikipedia.org/wiki/Quantum_logic_gate
"""
from Qubit import Qubit
from .Graph import *
import numpy as np
import random

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
            final_state (int): collapse matrix.
        """
        # get probabilities matrix from self.probabilities()
        probability_matrix = self.probabilities()
        # create a 1D array of the states, 2 ** n(qubits)
        bits = len(self._qubit_array) # number of bits
        state_list = [format(i, 'b').zfill(bits) for i in range(2**bits)] # creates a list of bits in strings
        state_list = list(map(int, state_list)) # turns state_list from list of strings to list of ints
        # create a temporary np.array to flatten the 2D probability_matrix into a 1D array which can
        # hold all the probabilities as weights
        temp_array = np.array(probability_matrix) 
        weight_list = temp_array.flatten()
        # numpy.random.choice takes in the list we will select from, size of the returning list,
        # and p = weights of each element 
        final_state = np.random.choice(state_list, 1, p = weight_list)
        final_state = final_state[0] # take out the bits from the returned list
        final_state = str(final_state) # turn the bits back into a string
        final_state = "|" + final_state + ">" # put the bits into ket notation
        return(final_state) # return the final state
    def probabilities(self):
        """
        Returns matrix with all probabilities for each state.
        Params:
            None
        Returns:
            probability_matrix (list): matrix with all weighted probabilities.
        """
        q = self._qubit_array.copy() # make a copy of self._qubit_array which will be used as a queue
        probability_matrix = np.square(q) #square all of the values in matrix to get probabilties of each qubit state
        if len(q) > 1: # tensor only if the length of self._qubit_array is greater than 1
            temp_matrix = np.kron(q[0].state, q[1].state) # create our temporary matrix
            # use numpy's Kronecker product on the first 2 qubit states and then delete them from the queue
            del q[0]
            del q[0]
            while q: # go through the rest of the queue
                temp_matrix = np.kron(temp_matrix, q[0].state)
                del q[0]
            # square all of the values in matrix to get probabilties of each qubit state
            probability_matrix = np.square(temp_matrix)
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