import numpy as np
from ..tools import *

"""
ControlledKronecker:
    Acts much like a Kronecker Product, however there is a need to have
    "flip states" determined by a standpoint from a control and target qubit
    calculation. At the end final 2^qubits state, it uses all flip states
    to finalize calculations.
"""

class ControlledKronecker:

    def __init__(self, qmace: object):
        # Takes in the correlated Qmace class object and takes values
        # it currently has.
    
        self._little_endian = qmace.get_little_endian()
        self._circuit_size = qmace.get_circuit_size()

        self._main_qubits = qmace.get_main_qubits()
        self._pair_qubits = qmace.get_pair_qubits()

        self._flip_state = qmace.get_flip_state()
        self._is_flip_state = qmace.get_is_flip_state()

        # result is used 
        self._result = []

        start = self._main_qubits[0]

        if (self._circuit_size == 1):
            self._result = start
            return
        
        new_state = np.zeros((2 ** len(self._main_qubits[0]), 1), 'F')
        state_length = 2
        index_of_qubits = 1

        while len(new_state) < 2**(self._circuit_size):
            
            index = 0

            while index < len(new_state):
                j = 0

                while j < len(start):
                    next_qubit_to_calculate = \
                        self._main_qubits[index_of_qubits]
                    k = 0
                    
                    while k < len(next_qubit_to_calculate):
                        
                        if (self._is_flip_state[index_of_qubits] and \
                            (index == self._flip_state[index_of_qubits])):


                            new_state[index] = start[j] * \
                                self._pair_qubits[index_of_qubits][k]
                            
                            index += 1
                            k += 1
                            new_state[index] = start[j] * \
                                self._pair_qubits[index_of_qubits][k]

                        else:
                            new_state[index] = start[j] * \
                                next_qubit_to_calculate[k]
                            
                        index += 1
                        k += 1

                    j += 1   

            start = new_state

            index_of_qubits += 1
            state_length += 1
            new_state = np.zeros((2 ** state_length, 1), 'F')

        """
        
        final procedure to add all of the values
        
        """

        index = 0
       
        while index < len(new_state):

            j = 0

            while j < len(start):
                next_qubit_to_calculate = \
                    self._main_qubits[index_of_qubits]
                k = 0
                while k < len(next_qubit_to_calculate):
                    
                    if (index in self._flip_state):
                        new_state[index] = start[j] * \
                            self._pair_qubits[index_of_qubits][k]
                        print(index)
                        index += 1
                        k += 1

                        new_state[index] = start[j] * \
                            self._pair_qubits[index_of_qubits][k]

                    else:
                        new_state[index] = start[j] * \
                            next_qubit_to_calculate[k]
                        
                    index += 1
                    k += 1

                j += 1 
        
        self._result = new_state
        return

    def amplitude(self):
        return

    def phaseangle(self):
        return

    def measure(self):
        return

    def probabilities(self):
        return

    def state(self):
        return self._result
