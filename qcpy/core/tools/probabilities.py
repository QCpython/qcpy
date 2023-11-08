from numpy import abs, around, multiply, square


def probabilities(state, circuit_size, show_percent: bool, show_bit: int = -1, round: int = 3):
    """
    Return a matrix with all the probabilities for each state
    Params:
        show_percent: bool
        show_bit: string or int
        round: int
    Returns:
        prob_matrix (numpy array):
            matrix with all the weighted probabilities of being measured
    """
    # determines if round is less than 0
    # if the
    if round < 0:
        exit(f"Error: QuantumCircuit.tools.probabilities() -- round placement must be a value greater than 0.")

    if type(show_bit) == int and show_bit < 0:
        probability = abs(square(state.flatten()))

    elif type(show_bit) == str or isinstance(show_bit, int):
        if type(show_bit) == str:
            show_bit = int(show_bit, 2)

        if 2**circuit_size <= show_bit:
            exit(
                f"Error: QuantumCircuit.tools.probabilities() -- Called bit to find phase angle is not within range of possible values."
            )

        probability = abs(square(state.flatten()[show_bit]))

    else:
        exit(
            f"Error: QuantumCircuit.tools.probabilities() -- show_bit given wrong type of value, binary string or integers in range are only allowed."
        )

    # get the probabilties for the "winner" of the measurement at any
    # single point on the circuit
    # collapse the circuit into 1D
    # square the values to get the probabilities of each qubit state
    # turn all the complex numbers into real values
    if show_percent:
        probability = multiply(probability, 100)
    return around(probability, decimals=round)
