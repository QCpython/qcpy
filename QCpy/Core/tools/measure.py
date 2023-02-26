from numpy import random, arange
def measure(state, circuit_size, probabilities):
    """
    Collapes the quantum circuit into classical bits
    Params:
        None
    Returns:
        final_state (str):
            the winning state displayed in classical bits notation
    """
    # randomly selects the measured state using self.probabilities()
    # number of bits
    # creates a list of bits in strings
    # numpy.random.choice takes in the list we will select from, size of the returning list,
    #  and p = weights of each element
    final_state = random.choice(arange(len(state), dtype=int), 1, p=probabilities)
    # take out the bits from the returned list and convert to a string
    final_state =str(bin(final_state[0]))[2:]
    # pad with zeroes if needed
    final_state = final_state.zfill(circuit_size)
    # return the final state
    return final_state