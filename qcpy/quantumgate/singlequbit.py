import numpy as np

"""
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

Phase Gate:
    Phase gate will rotate the qubit's amplitude based off of the value of theta.

S Gate:
    S gate is the equivalent to a pi / 2 rotation around the z axis for a qubit.

SDG Gate:
    DG gate is the inverse of the S gate and will change the qubits direction by -pi / 2 on the phase angle.

T Gate:
    T gate is a special use case gate that in implemented from the P Gate.

TDG Gate:
    TDG gate is the inverse of the T Gate that will impose the opposite rotation and shift of the gate.

RZ gate:
    RZ gate commits a rotation around the z-axis for a qubit.

RX Gate:
    RX gate commits a rotaiton around the x-axis for a given qubit.

RY Gate:
    RY gate commits a rotaiton around the y-axis for a given qubit.

SX Gate:
    SX gate in other terms is called a "square root of X (Inverse) gate" that creates a superposition of the qubit with a different positioning of the phase.

SXDG Gate:
    SXDG gate is the inverse of the SX gate and will inact the same logic as the SX but in a oppsite manner of what the original gate intended.

U Gate:
    U gate is given three inputs (theta, phi, and lambda) that allow the inputs to manipulate the base matrix to allow for the position of the enacted qubit
    around the bloch sphere representation.

"""


def identity():
    """
    Confirms the state of a qubit as well as used in expanding other gates to then be applied to a specific qubit within a quantum circuit.
    Matrix:
        I = [1, 0]
            [0, 1]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]], "F")


def paulix():
    """
    Switches the amplitude of the amplitudes of the states of |0> and |1>.
    Matrix:
        X = [0, 1]
            [1, 0]
    """
    return np.array([[0 + 0j, 1 + 0j], [1 + 0j, 0 + 0j]], "F")


def pauliy():
    """
    Changes the state of the qubit by pi around the y-axis of a Bloch Sphere.
    Matrix:
        Y = [0, -i]
            [i,  0]
    """
    return np.array([[0 + 0j, 0 - 1j], [0 + 1j, 0 + 0j]], "F")


def pauliz():
    """
    Changes the state of the qubit by pi around the y-axis of a Bloch Sphere.
    Matrix:
        Z = [1,  0]
            [0, -1]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, -1 + 0j]], "F")


def hadamard():
    """
    Hadamard gate puts the qubit that this gate has been enacted on into a
    superposition state.
    Matrix:
        Hadamard = [1,  1]
                   [1, -1] * (1/sqrt(2))
    """
    return np.array([[1 + 0j, 1 + 0j], [1 + 0j, -1 + 0j]], "F") * (1 / np.sqrt(2))


def phase(theta: float = np.pi / 2):
    """
    Phase gate will rotate the qubit's amplitude based off of the value of theta.
    Matrix:
        Phase = [1, 0]
                [0, e^(i * θ)]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this
        gate will shift the qubits position.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp(0 + 1j * theta)]], "F")


def s():
    """
    S gate is the equivalent to a pi / 2 rotation around the z axis for a qubit.
    Matrix:
        S = [1, 0]
            [0, i]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 + 1j]], "F")


def sdg():
    """
    SDG gate is the inverse of the S gate and will change the
    qubits direction by -pi / 2 on the phase angle.
    Matrix:
        SDG = [1, 0]
              [0, -i]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 - 1j]], "F")


def t():
    """
    T gate is a special use case gate that in implemented from the P Gate.
    Matrix:
        T = [1, 0]
            [0, e^((i * pi) / 4]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp((0 + 1j * np.pi) / 4)]], "F")


def tdg():
    """
    TDG gate is the inverse of the T Gate that will impose the opposite rotation
      and shift of the gate.
    Matrix:
        TDG = [1, 0]
              [0, e^((-i * pi) / 4]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp((0 - 1j * np.pi) / 4)]], "F")


def rz(theta: float = np.pi / 2):
    """
    RZ gate commits a rotation around the z-axis for a qubit.
    Matrix:
        RZ = [e^(-i * (θ / 2)), 0]
             [0,  e^(i * (θ / 2))]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate \
        will shift the qubits position.
    """
    return np.array([[np.exp((0 - 1j * (theta / 2))), 0 + 0j], [0 + 0j, np.exp(0 + 1j * (theta / 2))]], "F")


def rx(theta: float = np.pi / 2):
    """
    RX gate commits a rotaiton around the x-axis for a given qubit.
    Matrix:
        RX = [cos(θ / 2), -i * sin(θ / 2)]
             [-i * sin(θ / 2),  cos((θ / 2))]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate
        will shift the qubits position.
    """
    return np.array(
        [[np.cos(theta / 2), 0 - 1j * np.sin(theta / 2)], [0 - 1j * np.sin(theta / 2), np.cos(theta / 2)]], "F"
    )


def ry(theta: float = np.pi / 2):
    """
    RY gate commits a rotaiton around the y-axis for a given qubit.
    Matrix:
        RY = [cos(θ / 2), -1 * sin(θ / 2)]
             [sin(θ / 2),  cos((θ / 2))]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate
        will shift the qubits position.
    """
    return np.array([[np.cos(theta / 2), -1 * np.sin(theta / 2)], [np.sin(theta / 2), np.cos(theta / 2)]], "F")


def sx():
    """
    SX gate in other terms is called a "square root of X (Inverse) gate"
    that creates a superposition of the qubit with a different positioning
    of the phase.
    Matrix:
        SX = [1 + i, 1 - i]
             [1 - i, 1 + i] * (1 / 2)
    """
    return np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]], "F") * (1 / 2)


def sxdg():
    """
    SXDG gate is the inverse of the SX gate and will inact the same logic
    as the SX but in a oppsite manner of what the original gate intended.
    Matrix:
        SXDG = [1 - i, 1 + i]
               [1 + i, 1 - i] * (1 / 2)
    """
    return np.array([[1 - 1j, 1 + 1j], [1 + 1j, 1 - 1j]], "F") * (1 / 2)


def u(theta: float = np.pi / 2, phi: float = np.pi / 2, lmbda: float = np.pi / 2):
    """
    U gate is given three inputs (theta, phi, and lambda) that allow the inputs
    to manipulate the base matrix to allow for the position of the enacted qubit
    around the bloch sphere representation.
    Matrix:
        U = [cos(θ / 2), -1 * e^(i * λ) * sin(θ / 2)]
            [e^(i * φ) * sin(θ / 2), e^(i * (λ + φ)) * cos(θ / 2)]
    ...
    Args:
        theta: Initially set to pi / 2, can be inputted to change how this gate will shift the qubits position.
        phi: Initially set to pi / 2, can be inputted to change how this gate will shift the qubits position.
        lmbda: Initially set to pi / 2, can be inputted to change how this gate will shift the qubits position.
    """
    return np.array(
        [
            [np.cos(theta / 2), -1 * np.exp(0 + 1j * lmbda) * np.sin(theta / 2)],
            [np.exp(0 + 1j * phi) * np.sin(theta / 2), np.exp(0 + 1j * (lmbda + phi)) * np.cos(theta / 2)],
        ],
        "F",
    )
