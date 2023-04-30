import numpy as np
from QCpy import Qubit

def controller():

    num_qubits = 1
    qubits = [Qubit().state for _ in range(num_qubits)]

    start = qubits[0]
    new_state = np.zeros(2 ** len(qubits[0]), 'F')

    state_length = 2
    index_of_qubits = 1

    result = []
    if (num_qubits == 1):
        return Qubit().state
    
    while len(new_state) <= 2**num_qubits:

        reached_end = False
        index = 0

        while index < len(new_state) and reached_end == False:

            start = start.flatten()
            for j in range(len(start)):
                test = qubits[index_of_qubits].flatten()

                for k in range(len(test)):

                    new_state[index] = start[j] * test[k]
                    
                    index += 1


        result = new_state
        start = new_state
        index_of_qubits += 1
        state_length += 1
        if (not reached_end):
            new_state = np.zeros(2 **  state_length,'F')

    return result


print(controller())