import matplotlib.pyplot as plt
from .base.graph import graph
from ..tools import probability as prob
from ..tools.base import convert_state
import numpy as np


def probability(
    state: any,
    path: str = "probabilities.png",
    save: bool = False,
    show: bool = True,
    darkmode: bool = True,
):

    num_qubits = int(np.log2(len(convert_state(state))))
    state_list = [format(i, "b").zfill(num_qubits) for i in range(2**num_qubits)]
    percents = [i * 100 for i in prob(state)]
    if darkmode:
        _text = "white"
        _accent = "#39c0ba"
        _background = "#2e3037"
    else:
        _text = "black"
        _accent = "black"
        _background = "white"
    plt.clf()
    plt.close()
    ax = graph(_text, _background, num_qubits)
    ax.bar(state_list, percents, color="#39c0ba")
    plt.xlabel("Computational basis states", color=_accent)
    plt.ylabel("Probability (%)", labelpad=5, color=_accent)
    plt.title("Probabilities", pad=10, color=_accent)
    plt.tight_layout()
    if save:
        plt.savefig(path)
    if show:
        plt.show()
    return
