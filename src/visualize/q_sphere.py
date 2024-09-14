from collections import deque
import matplotlib.pyplot as plt
import numpy as np
from .base.sphere import sphere
from ..tools import probability, amplitude, phaseangle


def hamming_distance(l1: str, l2: str):
    return l1.count("1") == l2.count("1")


def latitude_finder(num_qubits: int, state_list):
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


def get_coords(num_qubits, lat_vals):
    coords = []
    phi = []
    theta = []
    for i in range(len(lat_vals)):
        temp_arr = np.linspace(
            2 * (np.pi) / len(lat_vals[i]), 2 * (np.pi), len(lat_vals[i])
        )
        theta.append(temp_arr)
    phi = np.linspace(0, np.pi, num_qubits + 1)
    for i in range(len(phi)):
        for j in range(len(theta[i])):
            x1 = 1 * np.sin(phi[i]) * np.cos(theta[i][j])
            y1 = 1 * np.sin(phi[i]) * np.sin(theta[i][j])
            z1 = 1 * np.cos(phi[i])
            x, y, z = [0, x1], [0, y1], [0, z1]
            coords.append([x, y, z])

    return coords


def q_sphere(
    quantumstate,
    path: str = "qsphere.png",
    save: bool = False,
    show: bool = True,
    darkmode: bool = True,
):
    num_qubits = int(np.log2((len(quantumstate.state))))
    probs = probability(quantumstate)
    angle = phaseangle(quantumstate)
    state_list = [format(i, "b").zfill(num_qubits) for i in range(2**num_qubits)]
    prob_dict = {state_list[i]: probs[i] for i in range(len(state_list))}
    phase_dict = {state_list[i]: angle[i] for i in range(len(state_list))}
    lat_vals = latitude_finder(num_qubits, state_list)
    if darkmode:
        _text = "white"
        _accent = "#39c0ba"
        _background = "#2e3037"
    else:
        _text = "black"
        _accent = "black"
        _background = "white"
    ax = sphere(_background)
    coords = get_coords(num_qubits, lat_vals)
    ham_states = [item for sublist in lat_vals for item in sublist]
    colors = plt.get_cmap("hsv")
    norm = plt.Normalize(0, np.pi * 2)
    for i, j in zip(coords, ham_states):
        cur_prob = prob_dict[j]
        cur_phase = phase_dict[j]
        if cur_prob > 0:
            x, y, z = i[0], i[1], i[2]
            ax.plot3D(x, y, z, color=colors(norm(cur_phase)))
            ax.scatter(x[1], y[1], z[1], s=5, color=colors(norm(cur_phase)))
            ax.text(x[1] * 1.15, y[1] * 1.15, z[1] * 1.15, f"|{j}>", color=_text)
    cbar = plt.colorbar(
        plt.cm.ScalarMappable(cmap=colors, norm=norm), ax=plt.gca(), shrink=0.55
    )
    cbar.set_label("Phase Angle", rotation=270, labelpad=15, color=_accent)
    cbar.set_ticks([2 * np.pi, (3 * np.pi) / 2, np.pi, np.pi / 2, 0])
    cbar.ax.yaxis.set_tick_params(color=_text)
    cbar.outline.set_edgecolor(_text)
    cbar.set_ticklabels(["2π", "3π / 2", "π", "π / 2", "0"], color=_text)
    plt.tight_layout()
    plt.axis("off")
    if save:
        plt.savefig(path)
    if show:
        plt.show()
    return
