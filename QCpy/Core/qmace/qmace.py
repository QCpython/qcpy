import numpy as np
from ...qubit import Qubit

"""
Qmace:
    Also known as QMACE (Quantum Math Accelerated Calculations and Efficiency),
    this is the core structuring for what the Controlled Kronocker needs to
    compute quantum computing math. 
"""

class Qmace:

    def __init__(self, qubits: int, little_endian: bool = False, prep: chr = 'z'):

        self._little_endian = little_endian
        self._circuit_size = qubits

        self._main_qubits = [Qubit(prep).state for _ in range(self._circuit_size)]
        self._pair_qubits = [Qubit(prep).state for _ in range(self._circuit_size)]
        

        self._is_flip_state = [False for _ in range(self._circuit_size)]
        self._flip_state = [-1 for _ in range(self._circuit_size)]
        self._child_qubits = [-1 for _ in range(self._circuit_size)]


    def merge_single_gate(self, qubit: int, single_qubit_gate: np.array):
        
        if self._child_qubits[qubit] == -1:
            self._main_qubits[qubit] = np.dot(single_qubit_gate, self._main_qubits[qubit])
            self._pair_qubits[qubit] = np.dot(single_qubit_gate, self._pair_qubits[qubit])
        else:
            self._main_qubits[self._child_qubits[qubit]] = \
            np.dot(single_qubit_gate, self._main_qubits[self._child_qubits[qubit]])

            self._pair_qubits[self._child_qubits[qubit]] = \
            np.dot(single_qubit_gate, self._pair_qubits[self._child_qubits[qubit]])

        return
    
    def merge_controlled_gate(self, control_qubit: int, target_qubit: int, single_qubit_gate: np.array):
        
        if self._main_qubits[control_qubit].all() != Qubit(initial_state = 'z').state.all():

            self._pair_qubits[target_qubit] = np.dot(single_qubit_gate, self._pair_qubits[target_qubit])

            self._is_flip_state[target_qubit] = True

            self._flip_state[target_qubit] = (2**(target_qubit)) # temporary bodge for basic testing, this will be set to just this value but without the  -2

            self._child_qubits[control_qubit] = target_qubit

        else:
            """
            Needs to be inserted. This will deal with 
            """
            return
        return
    
    def set_qubit(self, qubit: int, prep: chr = 'z'):

        self._main_qubits[qubit] = Qubit(prep).state
        return
    
    """ All of these need rework as simply calling the reverse of the result is not enough """
    def get_little_endian(self):
        return self._little_endian
    
    def get_circuit_size(self):
        return self._circuit_size
    
    def get_main_qubits(self):
        return self._main_qubits[::-1] if self._little_endian else self._main_qubits
    
    def get_pair_qubits(self):
        return self._pair_qubits[::-1] if self._little_endian else self._pair_qubits
    
    def get_flip_state(self):
        return self._flip_state[::-1] if self._little_endian else self._flip_state
    
    def get_is_flip_state(self):
        return self._is_flip_state[::-1] if self._little_endian else self._is_flip_state

    """ Needs to be deleted """

    def get_all(self):
        print("Main Qubits")
        for i in range(len(self._main_qubits)):
            print(i)
            print(self._main_qubits[i])
        print('----')
        print("Paired Qubits")
        for i in range(len(self._pair_qubits)):
            print(i)
            print(self._pair_qubits[i])
        print("Flip States")
        print(self._flip_state)
        print("Child Qubits")
        print(self._child_qubits)
        return

