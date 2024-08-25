from numpy import angle, around, mod, pi, log2
from .base import convert_state


def phase_angle(state, show_bit=-1, round: int = 3, radian: bool = True):
    size = int(log2(state.size))

    state = convert_state(state)
    if round < 0:
        exit(
            f"Error: QuantumCircuit.tools.phaseAngle() -- round placement must be a value greater than 0."
        )

    if type(show_bit) == int and show_bit < 0:
        phaseangle = mod(angle(state), 2 * pi) * (180 / pi)

    elif type(show_bit) == str or type(show_bit) == int:
        phaseangle = show_bit

        if type(show_bit) == str:
            phaseangle = int(show_bit, 2)
        if 2**size <= phaseangle:
            exit(
                f"Error: QuantumCircuit.tools.phaseAngle() -- Called bit to find phase angle is not within range of possible values."
            )

        phaseangle = mod(angle(state[phaseangle]), 2 * pi) * (180 / pi)
    else:
        exit(
            f"Error: QuantumCircuit.tools.phaseAngle() -- show_bit given wrong type of value, binary string or integers in range are only allowed."
        )

    if radian:
        phaseangle *= pi / 180

    return around(phaseangle, decimals=round)
