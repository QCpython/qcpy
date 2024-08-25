from numpy import arcsin, around, power, sqrt, log2
from .base import convert_state
from ..exception.tools_exception import ToolsException


def amplitude(quantumstate, show_bit=-1, round: int = 3, radian: bool = False):
    quantumstate = convert_state(quantumstate)
    size = int(log2(quantumstate.size))
    ToolsException().test_amplitude(show_bit, round, amplitude)
    if type(show_bit) == int and show_bit < 0:
        amplitude = sqrt(power(quantumstate.real, 2) + power(quantumstate.imag, 2))

    elif type(show_bit) == str or type(show_bit) == int:

        amplitude = show_bit
        if type(show_bit) == str:
            amplitude = int(show_bit, 2)
        amplitude = sqrt(
            power(quantumstate[amplitude].real, 2)
            + power(quantumstate[amplitude].imag, 2)
        )

    if radian:
        amplitude = arcsin(amplitude) * 2

    return around(amplitude, decimals=round)
