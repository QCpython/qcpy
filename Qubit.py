"""
Qubit.py
"""
import numpy as np
from sys import exit
"""
Purpose:
To initialize the values in the QuantumCircuit and to determine the angle of the initial state of the quantum wire.
Methods
--------
None.

"""
class Qubit:
    def __init__(self, initial_state: chr):
        """
        Args:
            initial_state:
                A character input of either x, y, z to indicate either the qubit's facing to be at either the z axis, y axis, or x axis in true whole value.
        ----
        Variables:
        _INITIAL_STATE: 
            Sets a variable in the class object from the argument to determine what the qubits facing is.
        state: 
            Is the variable to store the matrix of what the qubits starting face is and will be called from other systems to determine themselves.
        """
        self._INITIAL_STATE = initial_state
        self.state = None
        # Sets qubit to the z-axis and will face "upwards" or [1,0,...n^2 - 1].
        if(self._INITIAL_STATE == 'z'):
            self.state = np.array([[1+0j], [0+0j]])
            # Sets the qubit to the y-axis.
        elif(self._INITIAL_STATE == 'y'):
            self.state = np.array([[0+0j + 1+0j], [(1+0j + 0+0j) * 0+1j]]) / np.sqrt(2)
            # Sets the qubit to the y-axis.
        elif(self._INITIAL_STATE == 'x'):
            self.state = np.array([[0+0j + 1+0j], [1+0j + 0+0j]]) / np.sqrt(2)     
            # Calls error as no other plane of existence for calculations exists.    
        else:
            exit(f"Error: Qubit.__init__() -- Qubit must be initialized in a 0 or 1 state \n Qubit was initialized in state: {initial_state}.")