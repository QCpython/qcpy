"""
Qubit.py

A 2D vector representing the state of a single bit.
"""
class Qubit:
    def __init__(self, state: int):
        self._INIT_STATE = state # the state the qubit was init in
        self.state = None # state of the qubit
        # create 2x1 matrix for state
        if(state == 0):
            self.state = [[1+0j], [0+0j]]
        if(state == 1):
            self.state = [[0+0j], [1+0j]]
        