"""
QuantumGate.py

A collection of quantum gates used to manipulate the state.

-------

Identity:
    Confirms the state of a qubit as well as used in expanding other gates to then be applied to a specific qubit within a quantum circuit.

PauliX:
    Switches the amplitude of the amplitudes of the states of |0> and |1>

PauliY:
    Changes the state of the qubit by pi around the y-axis of a Bloch Sphere.

PauliZ:
    Changes the state of the qubit by pi around the z-axis of a Bloch Sphere.

Hadamard:
    Hadamard gate puts the qubit that this gate has been enacted on into a superposition state.

CNOT:
    CNOT Gate allows for two qubits to be entangled with each other if the control qubit is greater than 0.
    This gate needs to be formatted based off of whether or not it is being calculated in little or big endian format of bit measuring placement.

SWAP: 
    SWAP Gate allows for two qubits to swap its values and properties.

Toffoli Gate:
    Acts similar in nature to the CNOT gate and will entangle qubits together, only it has two control qubits instead of one.

Phase Gate:
    Phase gate will rotate the qubit's amplitude based off of the value of theta.

S Gate:
    S gate is the equivalent to a pi / 2 rotation around the z axis for a qubit.

SDG Gate:
    DG gate is the inverse of the S gate and will change the qubits direction by -pi / 2 on the phase angle.

T Gate:

TDG Gate:

RZ gate:

RX Gate:

RY Gate:

SX Gate:

SXDG Gate:

U Gate:

RXX Gate:

RZZ Gate:

CR Gate:

CZ Gate:


"""
import numpy as np

class Identity:
    """
    Confirms the state of a qubit as well as used in expanding other gates to then be applied to a specific qubit within a quantum circuit.
    Matrix:
        I = [1, 0]
            [0, 1]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for Identity gate.
    """
    def __init__(self):
        self.matrix = np.array([
                [1+0j, 0+0j], 
                [0+0j, 1+0j]
            ])
class PauliX:
    """
    Switches the amplitude of the amplitudes of the states of |0> and |1>.
    Matrix:
        X = [0, 1]
            [1, 0]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the Pauli-X gate.
    """
    def __init__(self):
        self.matrix = np.array([
                [0+0j, 1+0j], 
                [1+0j, 0+0j]
            ])
class PauliY:
    """
    Changes the state of the qubit by pi around the y-axis of a Bloch Sphere.
    Matrix:
        Y = [0, -i]
            [i,  0]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the Pauli-Y gate.
    """
    def __init__(self):
        self.matrix = np.array([
                [0+0j, 0-1j],
                [0+1j, 0+0j]
            ])
class PauliZ:
    """
    Changes the state of the qubit by pi around the y-axis of a Bloch Sphere.
    Matrix:
        Z = [1,  0] 
            [0, -1]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the Pauli-Z gate.
    """
    def __init__(self):
        self.matrix = ([
                [1+0j, 0+0j], 
                [0+0j, -1+0j]
            ])
class Hadamard:
    """
    Hadamard gate puts the qubit that this gate has been enacted on into a superposition state.
    Matrix:
        Hadamard = [1,  1] 
                   [1, -1] * (1/sqrt(2))
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the Hadamard gate.
    """
    def __init__(self):
        self.matrix = np.array([
                [1+0j, 1+0j], 
                [1+0J, -1+0j]
            ]) * (1/np.sqrt(2))
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
                ])
        else:
            self.matrix = np.array([
                    [1+0j, 0+0j, 0+0j, 0+0j],
                    [0+0j, 1+0j, 0+0j, 0+0j],
                    [0+0j, 0+0j, 0+0j, 1+0j],
                    [0+0j, 0+0j, 1+0j, 0+0j]
                ])
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
            ])
class Toffoli:
    """
    Toffoli Gate (CCX) acts similar in nature to the CNOT gate and will entangle qubits together, only it has two control qubits instead of one.

    Alongside the CNOT gate, the Toffoli gate needs to be implemented based off of the little or big endian assignment, which will be 
    implemented in a later feature.
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
            ])
class Phase:
    """
    Phase gate will rotate the qubit's amplitude based off of the value of theta.
    Matrix:
        Phase = [1, 0] 
                [0, e^(i * θ)]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate will shift the qubits position.
    ----
    Variables:
        self.matrix (numpy.Array): 
            matrix for the Phase gate.
    """
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, np.exp(0+1j * theta)]
        ])
class S:
    """
    S gate is the equivalent to a pi / 2 rotation around the z axis for a qubit.
    Matrix:
        S = [1, 0] 
            [0, i]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the S gate.
    """
    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, 0+1j]
        ])
class Sdg:
    """
    SDG gate is the inverse of the S gate and will change the qubits direction by -pi / 2 on the phase angle.
    Matrix:
        SDG = [1, 0] 
              [0, -i]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the SDG gate.
    """
    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, 0-1j]
        ])
class T:
    """
    T gate .
    Matrix:
        T = [1, 0] 
            [0, e^((i * pi) / 4]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the T gate.
    """
    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, np.exp((0+1j * np.pi) / 4)]
        ])
class Tdg:
    """
    TDG gate .
    Matrix:
        T = [1, 0] 
            [0, e^((-i * pi) / 4]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the TDG gate.
    """
    def __init__(self):
        self.matrix = np.array([
            [1+0j, 0+0j],
            [0+0j, np.exp((0-1j * np.pi) / 4)]
        ])
class Rz: #theta is equal to the rotation through angle phi around the z-axis
    """
    RZ gate .
    Matrix:
        RZ = [e^(-i * (θ / 2)), 0] 
             [0,  e^(i * (θ / 2))]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the RZ gate.
    """
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [np.exp((0-1j * (theta / 2))), 0+0j],
            [0+0j, np.exp(0+1j * (theta / 2))]
        ])
class Rx: #theta is equal to the rotation through angle phi around the x-axis
    """
    RX gate .
    Matrix:
        RX = [cos(θ / 2), -i * sin(θ / 2)] 
             [-i * sin(θ / 2),  cos((θ / 2))]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the RX gate.
    """
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [np.cos(theta / 2), 0-1j * np.sin(theta / 2)],
            [0-1j * np.sin(theta / 2), np.cos(theta / 2)]
        ])
class Ry: #theta is equal to the rotation through angle phi around the y-axis
    """
    RY gate .
    Matrix:
        RY = [cos(θ / 2), -1 * sin(θ / 2)] 
             [sin(θ / 2),  cos((θ / 2))]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the RY gate.
    """
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
            [np.cos(theta / 2), -1 * np.sin(theta / 2)],
            [np.sin(theta / 2), np.cos(theta / 2)]
        ])
class Sx:
    """
    SX gate .
    Matrix:
        SX = [1 + i, 1 - i] 
             [1 - i, 1 + i] * (1 / 2)
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the SX gate.
    """
    def __init__(self):
        self.matrix = np.array([
                [1+1j, 1-1j], 
                [1-1j, 1+1j]]) * (1 / 2)
class Sxdg:
    """
    SXDG gate .
    Matrix:
        SXDG = [1 - i, 1 + i] 
               [1 + i, 1 - i] * (1 / 2)
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the SXDG gate.
    """
    def __init__(self):
        self.matrix = np.array([
                [1-1j, 1+1j], 
                [1+1j, 1-1j]]) * (1 / 2)
class U:
    """
    U gate .
    Matrix:
        U = [cos(θ / 2), -1 * e^(i * λ) * sin(θ / 2)] 
            [e^(i * φ) * sin(θ / 2), e^(i * (λ + φ)) * cos(θ / 2)]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the U gate.
    """
    def __init__(self, theta: float = np.pi / 2, phi: float = np.pi / 2, lbmda: float = np.pi / 2):
        #-1 * np.e(0+1j * lbmda) * np.sin(theta / 2)
        self.matrix = np.array([
                [np.cos(theta / 2), -1 * np.exp(0+1j * lbmda) * np.sin(theta / 2)], 
                [np.exp(0+1j * phi) * np.sin(theta / 2), np.exp(0+1j * (lbmda + phi)) * np.cos(theta / 2)]])
class Rxx:
    """
    RXX gate .
    Matrix:
        RXX = [cos(θ / 2), 0, 0, -i * sin(θ / 2)]
              [0, cos(θ / 2), -i * sin(θ / 2), 0]
              [0, -i * sin(θ / 2), cos(θ / 2), 0]
              [-i * sin(θ / 2), 0, 0, cos(θ / 2)]
    ...
    Variables:
        self.matrix (numpy.Array): 
            matrix for the RXX gate.
    """
    def __init__(self, theta: float = np.pi / 2):
        self.matrix = np.array([
                [np.cos(theta / 2), 0+0j, 0+0j, 0-1j * np.sin(theta / 2)],
                [0+0j, np.cos(theta / 2), 0-1j * np.sin(theta / 2), 0+0j],
                [0+0j, 0-1j * np.sin(theta / 2), np.cos(theta / 2), 0+0j],
                [ 0-1j * np.sin(theta / 2), 0+0j, 0+0j, np.cos(theta / 2)]
            ])
class Rzz:
    """
    RZZ gate .
    Matrix:
        RZZ = [e^(-i * (θ / 2)), 0, 0, 0]
              [0,  e^(i * (θ / 2)), 0, 0]
              [0, 0,  e^(i * (θ / 2)), 0]
              [0, 0, 0, e^(-i * (θ / 2))]
    ...
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
            ])

class Cr:
    """
    CR gate .
    Matrix:
        CR = [1, 0, 0, 0]
             [0, 1, 0, 0]
             [0, 0, 1, 0]
             [0, 0, 0, e^(θ * i)]
    ...
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
        ])

class Cz:
    """
    CZ gate .
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
        ])
