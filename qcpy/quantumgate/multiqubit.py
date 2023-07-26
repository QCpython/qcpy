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

def cnot(little_endian: bool = False):
    """
    CNOT Gate allows for two qubits to be entangled with each other if the
    control qubit is greater than 0. This gate needs to be formatted based off
    of whether or not it is being calculated in little or big endian format of
    bit measuring placement.
    Matrix:
        CNOT in little endian form =  [1, 0, 0, 0]
                                      [0, 0, 0, 1]
                                      [0, 0, 1, 0]
                                      [0, 1, 0, 0]

        CNOT in big endian form =     [1, 0, 0, 0]
                                      [0, 1, 0, 0]
                                      [0, 0, 0, 1]
                                      [0, 0, 1, 0]
    """
    if little_endian:
        return np.array([
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j]
        ], 'F')
    else:
        return np.array([
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j]
        ], 'F')


def swap():
    """
    SWAP Gate allows for two qubits to swap its values and properties.
    (Ex: If one qubit is in a entangled state and is swapped with another,
    then the swapped qubit will be the entabled one.)
    Matrix:
        Swap = [1, 0, 0, 0]
               [0, 0, 1, 0]
               [0, 1, 0, 0]
               [0, 0, 0, 1]
    """
    return np.array([
        [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
        [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j]
    ], 'F')


def toffoli():
    """
    Toffoli Gate (CCX) acts similar in nature to the CNOT gate and will entangle
    qubits together, only it has two control qubits instead of one.

    Alongside the CNOT gate, the Toffoli gate needs to be implemented based off
    of the little or big endian assignment.
    Matrix:
        Toffoli = [1, 0, 0, 0, 0, 0, 0, 0]
                  [0, 1, 0, 0, 0, 0, 0, 0]
                  [0, 0, 1, 0, 0, 0, 0, 0]
                  [0, 0, 0, 1, 0, 0, 0, 0]
                  [0, 0, 0, 0, 1, 0, 0, 0]
                  [0, 0, 0, 0, 0, 1, 0, 0]
                  [0, 0, 0, 0, 0, 0, 0, 1]
                  [0, 0, 0, 0, 0, 0, 1, 0]
    """
    return np.array([
        [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j]
    ], 'F')


def rxx(theta: float = np.pi / 2):
    """
    RXX gate is a 2-qubit gate that will rotate both of the qubits around the
    x-axis at the same time.
    Matrix:
        RXX = [cos(θ / 2), 0, 0, -i * sin(θ / 2)]
              [0, cos(θ / 2), -i * sin(θ / 2), 0]
              [0, -i * sin(θ / 2), cos(θ / 2), 0]
              [-i * sin(θ / 2), 0, 0, cos(θ / 2)]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate
        will shift the qubits position.
    """
    return np.array([
        [np.cos(theta / 2), 0 + 0j, 0 + 0j, 0 - 1j * np.sin(theta / 2)],
        [0 + 0j, np.cos(theta / 2), 0 - 1j * np.sin(theta / 2), 0 + 0j],
        [0 + 0j, 0 - 1j * np.sin(theta / 2), np.cos(theta / 2), 0 + 0j],
        [0 - 1j * np.sin(theta / 2), 0 + 0j, 0 + 0j, np.cos(theta / 2)]
    ], 'F')


def rzz(theta: float = np.pi / 2):
    """
    RZZ gate is a 2-qubit gate that will rotate both of the qubits around the
    z-axis at the same time.
    Matrix:
        RZZ = [e^(-i * (θ / 2)), 0, 0, 0]
              [0,  e^(i * (θ / 2)), 0, 0]
              [0, 0,  e^(i * (θ / 2)), 0]
              [0, 0, 0, e^(-i * (θ / 2))]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate
        will shift the qubits position.
    """
    return np.array([
        [np.exp(0 - 1j * (theta / 2)), 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, np.exp(0 + 1j * (theta / 2)), 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, np.exp(0 + 1j * (theta / 2)), 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, np.exp(0 - 1j * (theta / 2))]
    ], 'F')


def cr(theta: float = np.pi / 2):
    """
    CR gate is a controlled phase shift roatation gate that applies to 2-qubits.
    Matrix:
        CR = [1, 0, 0, 0]
             [0, 1, 0, 0]
             [0, 0, 1, 0]
             [0, 0, 0, e^(θ * i)]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate
        will shift the qubits position.
    """
    return np.array([
        [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, np.exp(theta * 0 + 1j)]
    ], 'F')


def cz():
    """
    CZ gate is a controlled phase shift roatation gate that applies to 2-qubits.
    Matrix:
        CZ = [1, 0, 0, 0]
             [0, 1, 0, 0]
             [0, 0, 1, 0]
             [0, 0, 0, -1]
    """
    return np.array([
        [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
        [0 + 0j, 0 + 0j, 0 + 0j, -1 + 0j]
    ], 'F')
