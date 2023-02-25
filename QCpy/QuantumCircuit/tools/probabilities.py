from numpy import square, abs, around

def probabilities(state, round: int = 3):
    """
    Return a matrix with all the probabilities for each state
    Params:
        round: int
    Returns:
        prob_matrix (numpy array):
            matrix with all the weighted probabilities of being measured
    """
    if (round < 0):
        exit(f"Error: QuantumCircuit.tools.probabilities() -- round placement must be a value greater than 0.")
    # get the probabilties for the "winner" of the measurement at any
    # single point on the circuit
    # collapse the circuit into 1D
    # square the values to get the probabilities of each qubit state
    # turn all the complex numbers into real values
    prob_matrix = abs(square(state.flatten()))
    return around(prob_matrix, decimals=round)