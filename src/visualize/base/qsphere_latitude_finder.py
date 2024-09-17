from collections import deque
from .hamming_distance import hamming_distance


def qsphere_latitude_finder(num_qubits: int, state_list):
    latitude_values = [[]]
    for _ in range(num_qubits - 1):
        latitude_values.append([])
    latitude_values.append([])

    queue_of_state = deque(state_list)
    latitude_values[0].append(queue_of_state.popleft())
    latitude_values[-1].append(queue_of_state.pop())

    bit_representation = "0" * (num_qubits - 1) + "1"

    for i in range(1, len(bit_representation)):
        latitude_values[i].append(bit_representation)
        queue_of_state.remove(bit_representation)
        list_temp = list(bit_representation)
        list_temp[i - 1] = "1"
        bit_representation = "".join(list_temp)

    while queue_of_state:
        bit_representation = queue_of_state.popleft()
        for i in range(1, len(latitude_values) - 1):
            if hamming_distance(bit_representation, latitude_values[i][0]):
                latitude_values[i].append(bit_representation)

    return latitude_values
