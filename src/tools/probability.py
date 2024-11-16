from numpy import abs, around, multiply, square, log2, ndarray
from .base import convert_state
from typing import Union
from ..quantum_circuit import QuantumCircuit


def probability(
    quantum_state: Union[ndarray, QuantumCircuit],
    show_percent: bool = False,
    show_bit: int = -1,
    round: int = 3,
):
    circuit_size = int(log2(quantum_state.size))
    quantum_state = convert_state(quantum_state)
    if round < 0:
        RoundBelowZero(f"Cannot round to {round} needs to be 0 or greater")
    if isinstance(show_bit, int) and show_bit < 0:
        probability = abs(square(quantum_state))
    elif isinstance(show_bit, str) or isinstance(show_bit, int):
        if 2**circuit_size <= show_bit:
            OutOfRangeError(
                f"Cannot show bit of value {show_bit} as it is out of range"
            )
        probability = abs(square(quantum_state[show_bit]))
    if show_percent:
        probability = multiply(probability, 100)
    return around(probability, decimals=round)
