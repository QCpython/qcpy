import matplotlib.pyplot as plt
from numpy import pi, log2, ndarray, cos, sin, linspace
import math
from typing import Union
from ..quantum_circuit import QuantumCircuit
from .base import (
    sphere,
    color_bar,
    theme,
    light_mode,
)
from ..tools import probability, phaseangle


def q_sphere(
    quantum_state: Union[ndarray, QuantumCircuit],
    path: str = "qsphere.png",
    save: bool = False,
    show: bool = True,
    light: bool = False,
) -> None:
    colors = plt.get_cmap("hsv")
    norm = plt.Normalize(0, pi * 2)
    ax = sphere(theme.BACKGROUND_COLOR)
    light_mode(light)
    color_bar(plt, theme.TEXT_COLOR, theme.ACCENT_COLOR, colors, norm)
    prob_values = probability(quantum_state)
    phase_values = phaseangle(quantum_state)
    num_qubits = int(log2(len(prob_values)))
    bucket_array = [0] * (num_qubits + 1)
    phi_values = linspace(0, pi, num_qubits + 1)
    for i in range(len(prob_values)):
        if prob_values[i] > 0:
            binary_string = format(i, "b").zfill(num_qubits)
            bucket_index = binary_string.count("1")
            binomial_coeff = math.comb(num_qubits, bucket_index)
            inc_segment = 2 * pi / binomial_coeff
            lat_segments = inc_segment + bucket_array[bucket_index]
            bucket_array[bucket_index] += inc_segment
            x = [0, sin(phi_values[bucket_index]) * cos(lat_segments)]
            y = [0, sin(phi_values[bucket_index]) * sin(lat_segments)]
            z = [0, cos(phi_values[bucket_index])]
            ax.plot3D(x, y, z, color=colors(norm(phase_values[i])))
            ax.scatter(x[1], y[1], z[1], s=5, color=colors(norm(phase_values[i])))
            ax.text(
                x[1] * 1.15,
                y[1] * 1.15,
                z[1] * 1.15,
                f"|{binary_string}>",
                color=theme.TEXT_COLOR,
            )
    plt.tight_layout()
    plt.axis("off")
    if save:
        plt.savefig(path)
    if show:
        plt.show()
    return
