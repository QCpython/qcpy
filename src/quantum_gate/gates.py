import numpy as np


def identity():
    """
    I = [1, 0]
        [0, 1]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]], "F")


def paulix():
    """
    X = [0, 1]
        [1, 0]
    """
    return np.array([[0 + 0j, 1 + 0j], [1 + 0j, 0 + 0j]], "F")


def pauliy():
    """
    Y = [0, -i]
        [i,  0]
    """
    return np.array([[0 + 0j, 0 - 1j], [0 + 1j, 0 + 0j]], "F")


def pauliz():
    """
    Z = [1,  0]
        [0, -1]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, -1 + 0j]], "F")


def hadamard():
    """
    Hadamard = [1,  1]
               [1, -1] * (1/sqrt(2))
    """
    return np.array([[1 + 0j, 1 + 0j], [1 + 0j, -1 + 0j]], "F") * (1 / np.sqrt(2))


def phase(theta: float = np.pi / 2):
    """
    Phase = [1, 0]
            [0, e^(i * θ)]
    ...
    Args:
        theta: default pi / 2.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp(0 + 1j * theta)]], "F")


def s():
    """
    S = [1, 0]
        [0, i]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 + 1j]], "F")


def sdg():
    """
    SDG = [1, 0]
          [0, -i]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 - 1j]], "F")


def t():
    """
    T = [1, 0]
        [0, e^((i * pi) / 4]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp((0 + 1j * np.pi) / 4)]], "F")


def tdg():
    """
    TDG = [1, 0]
          [0, e^((-i * pi) / 4]
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp((0 - 1j * np.pi) / 4)]], "F")


def rz(theta: float = np.pi / 2):
    """
    RZ = [e^(-i * (θ / 2)), 0]
          [0,  e^(i * (θ / 2))]
    ...
    Args:
        theta: default pi / 2.
    """
    return np.array(
        [
            [np.exp((0 - 1j * (theta / 2))), 0 + 0j],
            [0 + 0j, np.exp(0 + 1j * (theta / 2))],
        ],
        "F",
    )


def rx(theta: float = np.pi / 2):
    """
    RX = [cos(θ / 2), -i * sin(θ / 2)]
          [-i * sin(θ / 2),  cos((θ / 2))]
    ...
    Args:
        theta: default pi / 2.
    """
    return np.array(
        [
            [np.cos(theta / 2), 0 - 1j * np.sin(theta / 2)],
            [0 - 1j * np.sin(theta / 2), np.cos(theta / 2)],
        ],
        "F",
    )


def ry(theta: float = np.pi / 2):
    """
    RY = [cos(θ / 2), -1 * sin(θ / 2)]
         [sin(θ / 2),  cos((θ / 2))]
    ...
    Args:
        theta: default pi / 2.
    """
    return np.array(
        [
            [np.cos(theta / 2), -1 * np.sin(theta / 2)],
            [np.sin(theta / 2), np.cos(theta / 2)],
        ],
        "F",
    )


def sx():
    """
    SX = [1 + i, 1 - i]
          [1 - i, 1 + i] * (1 / 2)
    """
    return np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]], "F") * (1 / 2)


def sxdg():
    """
    SXDG = [1 - i, 1 + i]
           [1 + i, 1 - i] * (1 / 2)
    """
    return np.array([[1 - 1j, 1 + 1j], [1 + 1j, 1 - 1j]], "F") * (1 / 2)


def u(theta: float = np.pi / 2, phi: float = np.pi / 2, lmbda: float = np.pi / 2):
    """
    U = [cos(θ / 2), -1 * e^(i * λ) * sin(θ / 2)]
        [e^(i * φ) * sin(θ / 2), e^(i * (λ + φ)) * cos(θ / 2)]
    ...
    Args:
        theta: default pi / 2.
        phi: default pi / 2.
        lmbda: default pi / 2.
    """
    return np.array(
        [
            [np.cos(theta / 2), -1 * np.exp(0 + 1j * lmbda) * np.sin(theta / 2)],
            [
                np.exp(0 + 1j * phi) * np.sin(theta / 2),
                np.exp(0 + 1j * (lmbda + phi)) * np.cos(theta / 2),
            ],
        ],
        "F",
    )


def r1(theta: float = np.pi / 2):
    """
    r1 =    [1, 0],
            [0, exp(iθ)]
    ...
    Args:
        theta: default pi / 2.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 + (1j * np.exp(theta))]], "F")


def cnot():
    """
    Matrix:
        CNOT little endian = [1, 0, 0, 0]
                             [0, 0, 0, 1]
                             [0, 0, 1, 0]
                             [0, 1, 0, 0]

        CNOT big endian = [1, 0, 0, 0]
                          [0, 1, 0, 0]
                          [0, 0, 0, 1]
                          [0, 0, 1, 0]
    """
    return np.array(
        [
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
        ],
        "F",
    )


def swap():
    """
    Matrix:
        Swap = [1, 0, 0, 0]
               [0, 0, 1, 0]
               [0, 1, 0, 0]
               [0, 0, 0, 1]
    """
    return np.array(
        [
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
        ],
        "F",
    )


def toffoli():
    """
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
    return np.array(
        [
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
        ],
        "F",
    )


def rxx(theta: float = np.pi / 2):
    """
    Matrix:
        RXX = [cos(θ / 2), 0, 0, -i * sin(θ / 2)]
              [0, cos(θ / 2), -i * sin(θ / 2), 0]
              [0, -i * sin(θ / 2), cos(θ / 2), 0]
              [-i * sin(θ / 2), 0, 0, cos(θ / 2)]
    ...
    Args:
        theta: default np.pi / 2
    """
    return np.array(
        [
            [np.cos(theta / 2), 0 + 0j, 0 + 0j, 0 - 1j * np.sin(theta / 2)],
            [0 + 0j, np.cos(theta / 2), 0 - 1j * np.sin(theta / 2), 0 + 0j],
            [0 + 0j, 0 - 1j * np.sin(theta / 2), np.cos(theta / 2), 0 + 0j],
            [0 - 1j * np.sin(theta / 2), 0 + 0j, 0 + 0j, np.cos(theta / 2)],
        ],
        "F",
    )


def rzz(theta: float = np.pi / 2):
    """
    Matrix:
        RZZ = [e^(-i * (θ / 2)), 0, 0, 0]
              [0,  e^(i * (θ / 2)), 0, 0]
              [0, 0,  e^(i * (θ / 2)), 0]
              [0, 0, 0, e^(-i * (θ / 2))]
    ...
    Args:
        theta: default np.pi / 2
    """
    return np.array(
        [
            [np.exp(0 - 1j * (theta / 2)), 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, np.exp(0 + 1j * (theta / 2)), 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, np.exp(0 + 1j * (theta / 2)), 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, np.exp(0 - 1j * (theta / 2))],
        ],
        "F",
    )


def cr(theta: float = np.pi / 2):
    """
    Matrix:
        CR = [1, 0, 0, 0]
             [0, 1, 0, 0]
             [0, 0, 1, 0]
             [0, 0, 0, e^(θ * i)]
    ...
    Args:
        theta: default np.pi / 2
    """
    return np.array(
        [
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, np.exp(theta * 0 + 1j)],
        ],
        "F",
    )


def cz():
    """
    Matrix:
        CZ = [1, 0, 0, 0]
             [0, 1, 0, 0]
             [0, 0, 1, 0]
             [0, 0, 0, -1]
    """
    return np.array(
        [
            [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
            [0 + 0j, 0 + 0j, 0 + 0j, -1 + 0j],
        ],
        "F",
    )
