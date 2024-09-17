import matplotlib.pyplot as plt
import numpy as np
from .base import (
    sphere,
    color_bar,
    theme,
    light_mode,
    qsphere_latitude_finder,
    get_qsphere_coordinates,
)
from ..tools import probability, phaseangle


def q_sphere(
    circuit: any,
    path: str = "qsphere.png",
    save: bool = False,
    show: bool = True,
    light: bool = False,
):
    num_qubits = int(np.log2((len(circuit.state))))
    probs = probability(circuit)
    angle = phaseangle(circuit)

    state_list = [format(i, "b").zfill(num_qubits) for i in range(2**num_qubits)]

    prob_dict = {state_list[i]: probs[i] for i in range(len(state_list))}
    phase_dict = {state_list[i]: angle[i] for i in range(len(state_list))}
    lat_vals = qsphere_latitude_finder(num_qubits, state_list)

    light_mode(light)
    ax = sphere(theme.BACKGROUND_COLOR)
    coords = get_qsphere_coordinates(num_qubits, lat_vals)
    ham_states = [item for sublist in lat_vals for item in sublist]
    colors = plt.get_cmap("hsv")
    norm = plt.Normalize(0, np.pi * 2)
    color_bar(plt, theme.TEXT_COLOR, theme.ACCENT_COLOR, colors, norm)

    for i, j in zip(coords, ham_states):
        cur_prob = prob_dict[j]
        cur_phase = phase_dict[j]
        if cur_prob > 0:
            x, y, z = i[0], i[1], i[2]
            ax.plot3D(x, y, z, color=colors(norm(cur_phase)))
            ax.scatter(x[1], y[1], z[1], s=5, color=colors(norm(cur_phase)))
            ax.text(
                x[1] * 1.15, y[1] * 1.15, z[1] * 1.15, f"|{j}>", color=theme.TEXT_COLOR
            )

    plt.tight_layout()
    plt.axis("off")
    if save:
        plt.savefig(path)
    if show:
        plt.show()

    return
