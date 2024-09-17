import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import rgb2hex
from .base.graph import graph
from ..tools import amplitude, phaseangle
from .base import color_bar, theme, light_mode


def state_vector(
    circuit: any,
    path: str = "statevector.png",
    save: bool = False,
    show: bool = True,
    light: bool = False,
):
    amplitudes = amplitude(circuit)
    phase_angles = phaseangle(circuit)
    num_qubits = int(np.log2(amplitudes.size))
    state_list = [format(i, "b").zfill(num_qubits) for i in range(2**num_qubits)]
    light_mode(light)
    ax = graph(theme.TEXT_COLOR, theme.BACKGROUND_COLOR, num_qubits)
    ax.set_ylim(0, np.amax(amplitudes))
    norm = plt.Normalize(0, np.pi * 2)
    colors = plt.get_cmap("hsv")
    color_bar(plt, theme.TEXT_COLOR, theme.ACCENT_COLOR, colors, norm)
    hex_arr = [rgb2hex(i) for i in colors(norm(phase_angles))]
    ax.bar(state_list, amplitudes, color=hex_arr)
    plt.xlabel("Computational basis states", color=theme.TEXT_COLOR)
    plt.ylabel("Amplitutde", labelpad=5, color=theme.TEXT_COLOR)
    plt.title("State Vector", pad=10, color=theme.TEXT_COLOR)

    plt.tight_layout()
    if save:
        plt.savefig(path)
    if show:
        plt.show()
    return
