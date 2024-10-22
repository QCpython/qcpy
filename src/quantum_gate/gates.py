import numpy as np
from numpy.typing import NDArray


def identity() -> NDArray:
    """Identity gate as a vector.

    ```
    I = [1, 0]
        [0, 1]
    ```
    Returns:
        NDArray: Vectorized identity gate.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]], "F")


def paulix() -> NDArray:
    """Pauli-X gate as a vector.

    ```
    X = [0, 1]
        [1, 0]
    ```
    Returns:
        NDArray: Vectorized pauli-x gate.
    """
    return np.array([[0 + 0j, 1 + 0j], [1 + 0j, 0 + 0j]], "F")


def pauliy() -> NDArray:
    """Pauli-Y gate as a vector.

    ```
    Y = [0, -i]
        [i,  0]
    ```
    Returns:
        NDArray: Vectorized pauli-y gate.
    """
    return np.array([[0 + 0j, 0 - 1j], [0 + 1j, 0 + 0j]], "F")


def pauliz() -> NDArray:
    """Pauli-Z gate as a vector.

    ```
    Z = [1,  0]
        [0, -1]
    ```
    Returns:
        NDArray: Vectorized pauli-z gate.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, -1 + 0j]], "F")


def hadamard() -> NDArray:
    """Hadamard gate as a vector.

    ```
    Hadamard = [1,  1]
               [1, -1] * (1/sqrt(2))
    ```
    Returns:
        NDArray: Vectorized hadamard gate.
    """
    return np.array([[1 + 0j, 1 + 0j], [1 + 0j, -1 + 0j]], "F") * (1 / np.sqrt(2))


def phase(theta: float = np.pi / 2) -> NDArray:
    """Phase gate as a vector.

    ```
    Phase = [1, 0]
            [0, e^(i * θ)]
    ```
    Args:
        theta (float, optional): Angle of vector. Defaults to np.pi/2.

    Returns:
        NDArray: Vectorized phase gate.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp(0 + 1j * theta)]], "F")


def s() -> NDArray:
    """S gate as a vector.

    ```
    S = [1, 0]
        [0, i]
    ```
    Returns:
        NDArray: Vectorized S gate.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 + 1j]], "F")


def sdg() -> NDArray:
    """SDG gate as a vector.

    ```
    SDG = [1, 0]
          [0, -i]
    ```
    Returns:
        NDArray: Vectorized SDG gate.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 - 1j]], "F")


def t() -> NDArray:
    """T gate as a vector.

    ```
    T = [1, 0]
        [0, e^((i * pi) / 4]
    ```
    Returns:
        NDArray: Vectorized T gate.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp((0 + 1j * np.pi) / 4)]], "F")


def tdg() -> NDArray:
    """TDG gate as a vector.

    ```
    TDG = [1, 0]
          [0, e^((-i * pi) / 4]
    ```
    Returns:
        NDArray: Vectorized TDG gate.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, np.exp((0 - 1j * np.pi) / 4)]], "F")


def rz(theta: float = np.pi / 2) -> NDArray:
    """RZ gate as a vector.

    ```
    RZ = [e^(-i * (θ / 2)), 0]
          [0,  e^(i * (θ / 2))]
    ```
    Args:
        theta (float, optional): Angle of vector. Defaults to np.pi/2.

    Returns:
        NDArray: Vectorized RZ gate.
    """
    return np.array(
        [
            [np.exp((0 - 1j * (theta / 2))), 0 + 0j],
            [0 + 0j, np.exp(0 + 1j * (theta / 2))],
        ],
        "F",
    )


def rx(theta: float = np.pi / 2) -> NDArray:
    """RX gate as a vector.

    ```
    RX = [cos(θ / 2), -i * sin(θ / 2)]
          [-i * sin(θ / 2),  cos((θ / 2))]
    ```
    Args:
        theta (float, optional): Angle of vector. Defaults to np.pi/2.

    Returns:
        NDArray: Vectorized RX gate.
    """
    return np.array(
        [
            [np.cos(theta / 2), 0 - 1j * np.sin(theta / 2)],
            [0 - 1j * np.sin(theta / 2), np.cos(theta / 2)],
        ],
        "F",
    )


def ry(theta: float = np.pi / 2) -> NDArray:
    """RY gate as a vector.


    ```
    RY = [cos(θ / 2), -1 * sin(θ / 2)]
         [sin(θ / 2),  cos((θ / 2))]
    ```
    Args:
        theta (float, optional): Angle of vector. Defaults to np.pi/2.

    Returns:
        NDArray: Vectorized RY gate.
    """
    return np.array(
        [
            [np.cos(theta / 2), -1 * np.sin(theta / 2)],
            [np.sin(theta / 2), np.cos(theta / 2)],
        ],
        "F",
    )


def sx() -> NDArray:
    """SX gate as a vector.

    ```
    SX = [1 + i, 1 - i]
          [1 - i, 1 + i] * (1 / 2)
    ```
    Returns:
        NDArray: Vectorized SX gate.
    """
    return np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]], "F") * (1 / 2)


def sxdg() -> NDArray:
    """SXDG gate as a vector.

    ```
    SXDG = [1 - i, 1 + i]
           [1 + i, 1 - i] * (1 / 2)
    ```
    Returns:
        NDArray: Vectorized SXDG gate.
    """
    return np.array([[1 - 1j, 1 + 1j], [1 + 1j, 1 - 1j]], "F") * (1 / 2)


def u(
    theta: float = np.pi / 2, phi: float = np.pi / 2, lmbda: float = np.pi / 2
) -> NDArray:
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


def r1(theta: float = np.pi / 2) -> NDArray:
    """
    r1 =    [1, 0],
            [0, exp(iθ)]
    ...
    Args:
        theta: default pi / 2.
    """
    return np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 + (1j * np.exp(theta))]], "F")


def cnot() -> NDArray:
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


def swap() -> NDArray:
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


def toffoli() -> NDArray:
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


def rxx(theta: float = np.pi / 2) -> NDArray:
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


def rzz(theta: float = np.pi / 2) -> NDArray:
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


def cr(theta: float = np.pi / 2) -> NDArray:
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


def cz() -> NDArray:
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
