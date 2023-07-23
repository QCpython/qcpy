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
        # defines endianness and number of qubits

        self._little_endian = qmace.get_little_endian()
        self._circuit_size = qmace.get_circuit_size()

        # main qubits and paired qubits are used in the kronecker product 
        # main qubits for when there is no flip state, and paired qubits 
        # for when there is a flip state

        self._main_qubits = qmace.get_main_qubits()
        self._pair_qubits = qmace.get_pair_qubits()

        # flip state is set to 2^(target qubit + 1), and will set to be 
        # 2^(target qubit + 1) - 2 in actual indexing format, and 
        #  (2^(target qubit + 1) + 2^(target qubit + 2) / 2) for the final iteration
        # of getting the qubits

        self._flip_state = qmace.get_flip_state()
        self._is_flip_state = qmace.get_is_flip_state()
        print(self._flip_state)
        # result is used to final product of the controlled kronecker product
        # and is used apart of class public methods (amplitude, probability, etc.)

        self._result = []

        # starting qubit to begin the process
        # if the number of qubits is just one, then no extra work
        # is needed and store the qubit vector inside of self._result

        start_sequence_qubit = self._main_qubits[0]

        if (self._circuit_size == 1):
            self._result = start_sequence_qubit
            return
        

        """
        NEEDS TO BE DONE:
            - tidy up the main switching componenets
            - show that when a qubit is within a entangled state,
            switch to normal kronecker product as it is not needed
                Going to make two methods to handle this and will be needed
                to change a lot of stuff
        
        """

        # sets a numpy array of zeros for new kronecker product 
        # new state_length to determine the added qubit onto the calcuation
        # index_of_qubits is set to one to start at q1 and proceed to qn

        new_quantum_circuit_state = np.zeros((2 ** len(self._main_qubits[0]), 1), 'F')
        new_quantum_circuit_state[0:1] = start_sequence_qubit
        state_length = 2
        qubit_array_index = 1

        # Go through the quantum state and continue to go through loop until the 
        # 2^(number of qubits) length is met, in which the final controlled 
        # kronecker product occurance will be completed

        while len(new_quantum_circuit_state) <= 2**(self._circuit_size):
            next_qubit_to_insert = self._main_qubits[qubit_array_index]
            if (not self._is_flip_state[qubit_array_index]):
                new_quantum_circuit_state = np.kron(next_qubit_to_insert, new_quantum_circuit_state)
            else:
                print("procedure here")
            qubit_array_index += 1
            state_length += 1
            self._result = new_quantum_circuit_state
            new_quantum_circuit_state = np.zeros((2 ** state_length, 1), 'F')
       
        
        
        return
    
    def __controlled_kronecker_product__(self):
        return
    
    def __kronecker_product__(self, qubit_index: int):
        return

    def amplitude(self):
        return

    def phaseangle(self):
        return

    def measure(self):
        return

    def probabilities(self):
        return

    def state(self, round: int = 3):
        return np.around(self._result, round)
