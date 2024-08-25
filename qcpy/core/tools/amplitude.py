from numpy import arcsin, around, power, sqrt


def amplitude(state, circuit_size, show_bit=-1, round: int = 3, radian: bool = False):
    """
    Return a vector of all possible amplitudes for the given state.
    Params:
        show_bit: string of binary values or integer
        round: int
        radian: bool
    Returns:
        np.around(statevector) (numpy array):
            Matrix after final calculation from the sqrt(x^2 + y^2) algorithm for finding the amplitude.
    """
    if round < 0:
        exit(
            f"Error: QuantumCircuit.tools.amplitude() -- round placement must be a value greater than 0."
        )
    if type(show_bit) == int and show_bit < 0:
        # for loop will go through this statement 2^n times for _state length
        # converts state to: (x^2 + y^2) where x is real values and y is imaginary values
        statevector = sqrt(power(state.real, 2) + power(state.imag, 2))

    # converts unsigned bit representation into a integer if string.
    # handles error for being out of bounds of 2^(num_of_qubits)
    # converts string bit to an integer to find the value for
    elif type(show_bit) == str or type(show_bit) == int:
        statevector = show_bit
        if type(show_bit) == str:
            statevector = int(show_bit, 2)

        if 2**circuit_size <= statevector:
            exit(
                f"Error: QuantumCircuit.tools.amplitude() -- Called bit to find amplitude is not within range of possible values."
            )
        statevector = sqrt(
            power(state[statevector].real, 2) + power(state[statevector].imag, 2)
        )
    # wrong value inputted for finding the show_bit
    else:
        exit(
            f"Error: QuantumCircuit.tools.amplitude() -- show_bit given wrong type of value, binary string or integer are only allowed."
        )
    if radian:
        statevector = arcsin(statevector) * 2
    return around(statevector, decimals=round)
