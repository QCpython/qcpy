from numpy import arange, random, log2
from .probability import probability
from .base import convert_state


def measure(state):
    state = convert_state(state)
    size = int(log2(state.size))
    probabilities = probability(state, round=size)
    final_state = random.choice(arange(len(state), dtype=int), 1, p=probabilities)
    final_state = str(bin(final_state[0]))[2:]
    final_state = final_state.zfill(size)
    return final_state
