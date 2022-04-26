"""
Qubit.py
"""
import numpy as np
from sys import exit

class Qubit:
    def __init__(self, initial_state: int):
        self._INITIAL_STATE = initial_state
        self.state = None
        if(initial_state == 0):
            self.state = np.array([[1+0j], [0+0j]])
        elif(initial_state == 1):
            self.state = np.array([[0+0j], [1+0j]])
        else:
            exit(f"Error: Qubit.__init__() -- Qubit must be initialized in a 0 or 1 state \n Qubit was initialized in state: {initial_state}")