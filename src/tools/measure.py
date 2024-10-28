from numpy import arange, random, log2, ndarray
from numpy.typing import NDArray
from typing import union
from .probability import probability
from .base import convert_state
from ..errors import *
from ..quantum_circuit import QuantumCircuit


def measure(quantumstate: Union[QuantumCircuit, ndarray]) -> NDArray:
    """Outputs the measure of a quantum circuit state.
    ```
    from qcpy import quantumcircuit, measure
    measure(quantumcircuit(qubits = 2)
    ```
    Returns:
        NDArray: Amplitude array from given state.
    """
    state = convert_state(quantumstate)
    size = int(log2(state.size))
    probabilities = probability(state, round=size)
    final_state = random.choice(arange(len(state), dtype=int), 1, p=probabilities)
    final_state = str(bin(final_state[0]))[2:]
    final_state = final_state.zfill(size)
    return final_state
