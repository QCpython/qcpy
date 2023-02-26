import numpy as np

"""
CNOT:
    CNOT Gate allows for two qubits to be entangled with each other if the control qubit is greater than 0.
    This gate needs to be formatted based off of whether or not it is being calculated in little or big endian format of bit measuring placement.

SWAP: 
    SWAP Gate allows for two qubits to swap its values and properties.

Toffoli Gate:
    Acts similar in nature to the CNOT gate and will entangle qubits together, only it has two control qubits instead of one.

RXX Gate:
    RXX gate is a 2-qubit gate that will rotate both of the qubits around the x-axis at the same time.

RZZ Gate:
    RZZ gate is a 2-qubit gate that will rotate both of the qubits around the z-axis at the same time.

CR Gate:
    CR gate is a controlled phase shift roatation gate that applies to 2-qubits.

CZ Gate:
    CZ gate is a controlled phase shift roatation gate that applies to 2-qubits.

"""

class CNot:
    """
    CNOT Gate allows for two qubits to be entangled with each other if the control qubit is greater than 0.
    This gate needs to be formatted based off of whether or not it is being calculated in little or big endian format of bit measuring placement.
    Matrix:
        CNOT in little endian form =  [1, 0, 0, 0] 
                                      [0, 0, 0, 1]
                                      [0, 0, 1, 0]
                                      [0, 1, 0, 0]

        CNOT in big endian form =     [1, 0, 0, 0]
                                      [0, 1, 0, 0]
                                      [0, 0, 0, 1]
                                      [0, 0, 1, 0]
    ...
    Variables:
        self.matrix (numpy.Array): 
            Matrix for the CNOT gate.
    """

    def __init__(self, inverse=False):
        if not inverse:
            self.matrix = np.array([
                [1+0j, 0+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 0+0j, 1+0j],
                [0+0j, 0+0j, 1+0j, 0+0j],
                [0+0j, 1+0j, 0+0j, 0+0j]
            ], 'F')
        else:
            self.matrix = np.array([
                [1+0j, 0+0j, 0+0j, 0+0j],
                [0+0j, 1+0j, 0+0j, 0+0j],
                [0+0j, 0+0j, 0+0j, 1+0j],
                [0+0j, 0+0j, 1+0j, 0+0j]
            ], 'F')
        self.symbol = 'Cnot'


class Swap:
    """
    SWAP Gate allows for two qubits to swap its values and properties. 
    (Ex: If one qubit is in a entangled state and is swapped with another, then the swapped qubit will be the entabled one.)
    Matrix:
        Swap = [1, 0, 0, 0]
               [0, 0, 1, 0]
               [0, 1, 0, 0]
               [0, 0, 0, 1]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the Swap gate.
    """

    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j, 0+0j, 0+0j],
            [0+0j, 0+0j, 1+0j, 0+0j],
            [0+0j, 1+0j, 0+0j, 0+0j],
            [0+0j, 0+0j, 0+0j, 1+0j]
        ], 'F')
        self.symbol = 'Swap'


class Toffoli:
    """
    Toffoli Gate (CCX) acts similar in nature to the CNOT gate and will entangle qubits together, only it has two control qubits instead of one.

    Alongside the CNOT gate, the Toffoli gate needs to be implemented based off of the little or big endian assignment.
    Matrix:
        Toffoli = [1, 0, 0, 0, 0, 0, 0, 0]
                  [0, 1, 0, 0, 0, 0, 0, 0]
                  [0, 0, 1, 0, 0, 0, 0, 0]
                  [0, 0, 0, 1, 0, 0, 0, 0]
                  [0, 0, 0, 0, 1, 0, 0, 0]
                  [0, 0, 0, 0, 0, 1, 0, 0]
                  [0, 0, 0, 0, 0, 0, 0, 1]
                  [0, 0, 0, 0, 0, 0, 1, 0]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the Toffoli gate.
    """

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
        ], 'F')
        self.symbol = 'Toffoli'

class Rxx:
    """
    RXX gate is a 2-qubit gate that will rotate both of the qubits around the x-axis at the same time.
    Matrix:
        RXX = [cos(θ / 2), 0, 0, -i * sin(θ / 2)]
              [0, cos(θ / 2), -i * sin(θ / 2), 0]
              [0, -i * sin(θ / 2), cos(θ / 2), 0]
              [-i * sin(θ / 2), 0, 0, cos(θ / 2)]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate will shift the qubits position.
    ----
    Variables:
        self.matrix (numpy.Array): 
            matrix for the RXX gate.
    """

    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [np.cos(theta / 2), 0+0j, 0+0j, 0-1j * np.sin(theta / 2)],
            [0+0j, np.cos(theta / 2), 0-1j * np.sin(theta / 2), 0+0j],
            [0+0j, 0-1j * np.sin(theta / 2), np.cos(theta / 2), 0+0j],
            [0-1j * np.sin(theta / 2), 0+0j, 0+0j, np.cos(theta / 2)]
        ], 'F')
        self.symbol = 'Rxx'


class Rzz:
    """
    RZZ gate is a 2-qubit gate that will rotate both of the qubits around the z-axis at the same time.
    Matrix:
        RZZ = [e^(-i * (θ / 2)), 0, 0, 0]
              [0,  e^(i * (θ / 2)), 0, 0]
              [0, 0,  e^(i * (θ / 2)), 0]
              [0, 0, 0, e^(-i * (θ / 2))]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate will shift the qubits position.
    ----
    Variables:
        self.matrix (numpy.Array): 
            matrix for the RZZ gate.
    """

    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [np.exp(0-1j * (theta / 2)), 0+0j, 0+0j, 0+0j],
            [0+0j, np.exp(0+1j * (theta / 2)), 0+0j, 0+0j],
            [0+0j, 0+0j, np.exp(0+1j * (theta / 2)), 0+0j],
            [0+0j, 0+0j, 0+0j, np.exp(0-1j * (theta / 2))]
        ], 'F')
        self.symbol = 'Rzz'


class Cr:
    """
    CR gate is a controlled phase shift roatation gate that applies to 2-qubits.
    Matrix:
        CR = [1, 0, 0, 0]
             [0, 1, 0, 0]
             [0, 0, 1, 0]
             [0, 0, 0, e^(θ * i)]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate will shift the qubits position.
    ----
    Variables:
        self.matrix (numpy.Array): 
            matrix for the CR gate.
    """

    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [1+0j, 0+0j, 0+0j, 0+0j],
            [0+0j, 1+0j, 0+0j, 0+0j],
            [0+0j, 0+0j, 1+0j, 0+0j],
            [0+0j, 0+0j, 0+0j, np.exp(theta * 0+1j)]
        ], 'F')
        self.symbol = 'Cr'


class Cz:
    """
    CZ gate is a controlled phase shift roatation gate that applies to 2-qubits.
    Matrix:
        CZ = [1, 0, 0, 0]
             [0, 1, 0, 0]
             [0, 0, 1, 0]
             [0, 0, 0, -1]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the CZ gate.
    """

    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j, 0+0j, 0+0j],
            [0+0j, 1+0j, 0+0j, 0+0j],
            [0+0j, 0+0j, 1+0j, 0+0j],
            [0+0j, 0+0j, 0+0j, -1+0j]
        ], 'F')
        self.symbol = 'Cz'