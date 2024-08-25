import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import rgb2hex
from .base.graph import graph
from ..tools import amplitude, phase_angle


def statevector(
    circuit: np.array,
    path: str = "statevector.png",
    save: bool = True,
    show: bool = False,
    darkmode: bool = True,
):
    num_qubits = int(np.log2(circuit.size))
    state_list = [format(i, "b").zfill(num_qubits) for i in range(2**num_qubits)]
    amplitutes = amplitude(circuit, num_qubits)
    phase_angles = phase_angle(circuit, num_qubits)
    if darkmode:
        _text = "white"
        _accent = "#39c0ba"
        _background = "#2e3037"
    else:
        _text = "black"
        _accent = "black"
        _background = "white"
    ax = graph(_text, _background, num_qubits)
    ax.set_ylim(0, np.amax(amplitutes))
    colors = plt.get_cmap("hsv")
    norm = plt.Normalize(0, np.pi * 2)
    hex_arr = [rgb2hex(i) for i in colors(norm(phase_angles))]
    ax.bar(state_list, amplitutes, color=hex_arr)
    plt.xlabel("Computational basis states", color=_accent)
    plt.ylabel("Amplitutde", labelpad=5, color=_accent)
    plt.title("State Vector", pad=10, color=_accent)
    cbar = plt.colorbar(ScalarMappable(cmap=colors, norm=norm))
    cbar.set_label("Phase Angle", rotation=270, labelpad=10, color=_accent)
    cbar.set_ticks([2 * np.pi, (3 * np.pi) / 2, np.pi, np.pi / 2, 0])
    cbar.ax.yaxis.set_tick_params(color=_text)
    cbar.outline.set_edgecolor(_text)
    cbar.set_ticklabels(["2π", "3π / 2", "π", "π / 2", "0"], color=_text)
    plt.tight_layout()
    if save:
        plt.savefig(path)
    if show:
        plt.show()
    return
