"""
Qubit.py
"""
from sys import exit

import numpy as np

"""
Purpose:
To initialize the values in the QuantumCircuit and to determine the
angle of the initial state of the quantum wire.
Methods
--------
None.

"""


def qubit(initial_state: chr = "z"):
    """
    Args:
        initial_state:
            A character input of either x, y, z to indicate either the ]
            qubit's facing to be at either the z axis, y axis, or x axis in
            true whole value.
    """
    # Sets qubit to the z-axis and will face "upwards" or [1,0,...n^2 - 1].
    if initial_state == "z":
        return np.array([[1 + 0j], [0 + 0j]], "F")
        # Sets the qubit to the y-axis.
    elif initial_state == "y":
        return np.array([[0 + 0j + 1 + 0j], [(1 + 0j + 0 + 0j) * 0 + 1j]], "F") / np.sqrt(2)
        # Sets the qubit to the y-axis.
    elif initial_state == "x":
        return np.array([[0 + 0j + 1 + 0j], [1 + 0j + 0 + 0j]], "F") / np.sqrt(2)
        # Calls error as no other plane of existence for calculations exists.
    else:
        exit(
            f"Error: Qubit.__init__() -- Qubit must be initialized in a 0 \
                or 1 state \n Qubit was initialized in state: {initial_state}."
        )
