from numpy import abs, around, multiply, square, log2
from .base import convert_state


def probability(
    quantumstate, show_percent: bool = False, show_bit: int = -1, round: int = 3
):

    circuit_size = int(log2(quantumstate.size))
    quantumstate = convert_state(quantumstate)
    if round < 0:
        exit(
            f"Error: QuantumCircuit.tools.probabilities() -- round placement must be a value greater than 0."
        )

    if type(show_bit) == int and show_bit < 0:
        probability = abs(square(quantumstate))

    elif type(show_bit) == str or isinstance(show_bit, int):

        if 2**circuit_size <= show_bit:
            exit(
                f"Error: QuantumCircuit.tools.probabilities() -- Called bit to find phase angle is not within range of possible values."
            )
        probability = abs(square(quantumstate[show_bit]))

    if show_percent:
        probability = multiply(probability, 100)

    return around(probability, decimals=round)
