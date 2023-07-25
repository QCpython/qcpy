from numpy import mod, pi, around, angle

def phaseangle(state, circuit_size, show_bit = -1, round: int = 3, radian: bool = True):
    """
    Calculates an array of possible phase angles based off the state. Converts each value using np.angle() function then degree to radian.
    Params:
        round: int
        radian: bool
    Returns:
        np.around(phaseAngles) (numpy array):
            Matrix after final calculation from the  phase angle algorithm.
    """
    # if rounding value is less than 0, exits as this is improper.
    if (round < 0):
        exit(f"Error: QuantumCircuit.tools.phaseAngle() -- round placement must be a value greater than 0.")

    if (type(show_bit) == int and show_bit < 0):

        phaseangle = (mod(angle(state), 2 * pi) * (180 / pi))

    elif (type(show_bit) == str or type(show_bit) == int):

        phaseangle = show_bit

        if (type(show_bit) == str):

            phaseangle = int(show_bit, 2)
        if (2**circuit_size <= phaseangle):

            exit(f"Error: QuantumCircuit.tools.phaseAngle() -- Called bit to find phase angle is not within range of possible values.")

        phaseangle = mod(angle(state[phaseangle]), 2 * pi) * (180 / pi)
    else:
        exit(f"Error: QuantumCircuit.tools.phaseAngle() -- show_bit given wrong type of value, binary string or integers in range are only allowed.")

    if (radian):
        phaseangle *= (pi / 180)
        
    return around(phaseangle, decimals = round)