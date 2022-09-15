"""
Qubit.py
"""
import numpy as np
from sys import exit
class Qubit:
    def __init__(self, initial_state: chr):
        self._INITIAL_STATE = initial_state
        self.state = None
        if(initial_state == 'z'):
            self.state = np.array([[1+0j], [0+0j]])
        elif(initial_state == 'y'):
            self.state = np.array([[0+0j + 1+0j], [(1+0j + 0+0j) * 0+1j]]) / np.sqrt(2)
        elif(initial_state == 'x'):
            self.state = np.array([[0+0j + 1+0j], [1+0j + 0+0j]]) / np.sqrt(2)        
        else:
            exit(f"Error: Qubit.__init__() -- Qubit must be initialized in a 0 or 1 state \n Qubit was initialized in state: {initial_state}")