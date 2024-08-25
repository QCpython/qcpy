import matplotlib.pyplot as plt
import numpy as np
from .base import sphere
from ..tools import probability, amplitude


def bloch(
    quantumstate=np.array,
    path: str = "BlochSphere.png",
    save: bool = False,
    show: bool = True,
    darkmode: bool = True,
):
    if np.log2(len(quantumstate)) > 1:
        exit(
            f"Error: BlochSphere() --", f"BlochSphere only calculates 1 qubit circuits."
        )
    amplitutes = amplitude(quantumstate)
    phase_angles = probability(quantumstate, False)
    if darkmode:
        _text = "white"
        _accent = "#39c0ba"
        _background = "#2e3037"
    else:
        _text = "black"
        _accent = "black"
        _background = "white"
    ax = sphere(_background)
    ax.quiver(1, 0, 0, 0.75, 0, 0, color="lightgray")
    ax.text(2, 0, 0, "+x", color="gray")
    ax.quiver(0, 1, 0, 0, 0.75, 0, color="lightgray")
    ax.text(0, 2, 0, "+y", color="gray")
    ax.quiver(0, 0, 1, 0, 0, 0.75, color="lightgray")
    ax.text(0, 0, 2, "+z", color="gray")
    ax.text(0.1, 0, 1.5, "|0>", color="gray")
    ax.quiver(0, 0, -1, 0, 0, -0.75, color="lightgray")
    ax.text(0, 0, -2, "-z", color="gray")
    ax.text(0.1, 0, -1.5, "|1>", color="gray")
    theta = np.arcsin(amplitutes[1]) * 2
    phi = phase_angles[1]
    x = 1 * np.sin(theta) * np.cos(phi)
    y = 1 * np.sin(theta) * np.sin(phi)
    z = 1 * np.cos(theta)
    xs, ys, zs = [0, x], [0, y], [0, z]
    ax.plot3D(xs, ys, zs, color=_accent)
    ax.scatter(xs[1], ys[1], zs[1], s=5, color=_accent)
    ax.text(xs[1] * 1.15, ys[1] * 1.15, zs[1] * 1.15, "|ψ⟩", color=_text)
    plt.tight_layout()
    plt.axis("off")
    if save:
        plt.savefig(path)
    if show:
        plt.show()
    return
