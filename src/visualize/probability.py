import matplotlib.pyplot as plt
from .base import graph, light_mode, theme
from ..tools import probability as prob
import numpy as np


def probability(
    state: any,
    path: str = "probabilities.png",
    save: bool = False,
    show: bool = True,
    light: bool = False,
):
    probabilities = prob(state)
    num_qubits = int(np.log2(probabilities.size))
    state_list = [format(i, "b").zfill(num_qubits) for i in range(2**num_qubits)]
    percents = [i * 100 for i in probabilities]

    plt.clf()
    plt.close()

    light_mode(light)
    ax = graph(theme.TEXT_COLOR, theme.BACKGROUND_COLOR, num_qubits)
    ax.bar(state_list, percents, color="#39c0ba")

    plt.xlabel("Computational basis states", color=theme.ACCENT_COLOR)
    plt.ylabel("Probability (%)", labelpad=5, color=theme.ACCENT_COLOR)
    plt.title("Probabilities", pad=10, color=theme.ACCENT_COLOR)
    plt.tight_layout()

    if save:
        plt.savefig(path)
    if show:
        plt.show()

    return
