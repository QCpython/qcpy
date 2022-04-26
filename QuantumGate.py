"""
QuantumGate.py
"""
import numpy as np
from math import sqrt

class Identity:
    """
    Applying this gate has no effect on the qubit state, outputting the same state.
    Matrix:
        I = [1 0]
            [0 1]
    ...
    self.matrix (numpy.Array): matrix for Identity gate.
    """
    def __init__(self):
        self.matrix = np.array([
                [1+0j, 0+0j], 
                [0+0j, 1+0j]
            ])
class PauliX:
    """
    Applying this gate inverses the amplitude of the qubit state.
    Matrix:
        X = [0 1]
            [1 0]
    ...
    self.matrix (numpy.Array): matrix for the Pauli-X gate.
    """
    def __init__(self):
        self.matrix = np.array([
                [0+0j, 1+0j], 
                [1+0j, 0+0j]
            ])
class PauliY:
    def __init__(self):
        self.matrix = np.array([
                [0+0j, 0-1j],
                [0+1j, 0+0j]
            ])
class PauliZ:
    def __init__(self):
        self.matrix = ([
                [1+0j, 0+0j], 
                [0+0j, -1+0j]
            ])
class Hadamard:
    def __init__(self):
        self.matrix = np.array([
                [1+0j, 1+0j], 
                [1+0J, -1+0j]
            ]) * (1/np.sqrt(2))
#Please take note this is technically not the right CNOT gate, hwoever IBM and Qiskit use it, so might need to ask someone
class CNot:
    def __init__(self, inverse=False):
        if not inverse:
            self.matrix = np.array([
                    [1+0j, 0+0j, 0+0j, 0+0j],
                    [0+0j, 0+0j, 0+0j, 1+0j],
                    [0+0j, 0+0j, 1+0j, 0+0j],
                    [0+0j, 1+0j, 0+0j, 0+0j]
                ])
        else:
            self.matrix = np.array([
                    [1+0j, 0+0j, 0+0j, 0+0j],
                    [0+0j, 0+0j, 0+0j, 1+0j],
                    [0+0j, 0+0j, 0+0j, 1+0j],
                    [0+0j, 1+0j, 1+0j, 0+0j]
                ])
class Swap:
    def __init__(self):
        self.matrix = np.array([
                [1+0j, 0+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 1+0j, 0+0j],
                [0+0j, 1+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 0+0j, 1+0j]
            ])
class Toffoli:
    def __init__(self):
        self.matrix = np.array([
                [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
                [0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j],
                [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j]
            ])
class Phase: #theta is the radians used to perform the rotation around the Z-axis
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, np.exp(0+1j * theta)]
        ])
class S:
    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, 0+1j]
        ])
class Sdg:
    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, 0-1j]
        ])
class T:
    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, np.e ** ((0+1j * np.pi) / 4)]
        ])
class Tdg:
    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, np.e ** ((0-1j * np.pi) / 4)]
        ])
class Rz: #theta is equal to the rotation through angle phi around the z-axis
    def __init__(self, theta: float):
        self.matrix = np.array([
            [np.exp((0-1j * (theta / 2))), 0+0j],
            [0+0j, np.exp(0+1j * (theta / 2))]
        ])
class Rx: #theta is equal to the rotation through angle phi around the x-axis
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [np.cos(theta / 2), 0-1j * np.sin(theta / 2)],
            [0-1j * np.sin(theta / 2), np.cos(theta / 2)]
        ])
class Ry: #theta is equal to the rotation through angle phi around the y-axis
    def __init__(self, theta: float):
        self.matrix = np.array([
            [np.cos(theta / 2), -1 * np.sin(theta / 2)],
            [np.sin(theta / 2), np.cos(theta / 2)]
        ])
class Sx:
    def __init__(self):
        self.matrix = np.array([
                [1+1j, 1-1j], 
                [1-1j, 1+1j]]) * (1 / 2)
class Sxdg:
    def __init__(self):
        self.matrix = np.array([
                [1-1j, 1+1j], 
                [1+1j, 1-1j]]) * (1 / 2)
class U:
    def __init__(self, theta: float = np.pi / 2, phi: float = np.pi / 2, lbmda: float = np.pi / 2):
        #-1 * np.e(0+1j * lbmda) * np.sin(theta / 2)
        self.matrix = np.array([
                [np.cos(theta / 2), -1 * np.exp(0+1j * lbmda) * np.sin(theta / 2)], 
                [np.exp(0+1j * phi) * np.sin(theta / 2), np.exp(0+1j * (lbmda + phi)) * np.cos(theta / 2)]])
class Rxx:
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
                [np.cos(theta / 2), 0+0j, 0+0j, 0-1j * np.sin(theta / 2)],
                [0+0j, np.cos(theta / 2), 0-1j * np.sin(theta / 2), 0+0j],
                [0+0j, 0-1j * np.sin(theta / 2), np.cos(theta / 2), 0+0j],
                [ 0-1j * np.sin(theta / 2), 0+0j, 0+0j, np.cos(theta / 2)]
            ])
class Rzz:
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
                [np.exp(0-1j * (theta / 2)), 0+0j, 0+0j, 0+0j],
                [0+0j, np.exp(0+1j * (theta / 2)), 0+0j, 0+0j],
                [0+0j, 0+0j, np.exp(0+1j * (theta / 2)), 0+0j],
                [0+0j, 0+0j, 0+0j, np.exp(0-1j * (theta / 2))]
            ])