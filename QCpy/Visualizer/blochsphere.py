import numpy as np
from ..Core import QuantumCircuit
import matplotlib.pyplot as plt
from .tools.sphere import Sphere


class BlochSphere:
    """
    Visualizes the quantum state of a single qubit as a sphere

    Methods
    --------
    makeSphere():
        returns a Bloch Sphere that plots the quantum state of a single qubit in a
        3D global view
    """

    def __init__(self, circuit=None, blochQubit=None):
        """
        Args:
            circuit:
                the quantum circuit
            blochQubit:
                the qubit that will be visualized
        ------
        Variables:
            _amplitudes :
                an array of the amplitude for every state
            _phase_angles :
                an array of the phase angle for every state
        """
        if (circuit.circuitSize() > 1):
            exit(
                f"Error: BlochSphere() -- BlochSphere only calculates 1 qubit circuits.")
        self._amplitutes = circuit.amplitude().flatten()
        self._phase_angles = circuit.phaseAngle().flatten()

    def makeSphere(
            self,
            path: str = "BlochSphere.png",
            show_bit: int = 0,
            save: bool = False,
            show: bool = True,
            darkmode: bool = True):
        """
            Creates a bloch sphere that visualizes a qubit's state in a 3D view
        Args:
            path (str): name of the image to be saved
            show_bit (int): the qubit on the circuit to be visualized, initialized as the 0th bit
            save (bool): pass True for the graph to be saved
            show (bool): pass True for the sphere to be shown instead of saved
            darkmode (bool): pass True for darkmode, false for lightmode
        """
        # sets up darkmode or lightmode
        if darkmode:
            _text = 'white'
            _accent = '#39c0ba'
            _background = '#2e3037'
        else:
            _text = 'black'
            _accent = 'black'
            _background = 'white'

        # creates a sphere
        ax = Sphere(_background)
        # x-axis arrow
        ax.quiver(1, 0, 0, .75, 0, 0, color="lightgray")
        ax.text(2, 0, 0, "+x", color="gray")
        # y-axis arrow
        ax.quiver(0, 1, 0, 0, .75, 0, color="lightgray")
        ax.text(0, 2, 0, "+y", color="gray")
        # +z and |0> arrow
        ax.quiver(0, 0, 1, 0, 0, .75, color="lightgray")
        ax.text(0, 0, 2, "+z", color="gray")
        ax.text(.1, 0, 1.5, "|0>", color="gray")
        # -z and |1> arrow
        ax.quiver(0, 0, -1, 0, 0, -.75, color="lightgray")
        ax.text(0, 0, -2, "-z", color="gray")
        ax.text(.1, 0, -1.5, "|1>", color="gray")

        # gets theta and phi values, theta is converted to radians
        theta = np.arcsin(self._amplitutes[1]) * 2
        phi = self._phase_angles[1]

        # gets x, y, z cartesian coords
        x = 1 * np.sin(theta) * np.cos(phi)
        y = 1 * np.sin(theta) * np.sin(phi)
        z = 1 * np.cos(theta)
        # plots a line from center to surface
        xs, ys, zs = [0, x], [0, y], [0, z]
        ax.plot3D(xs, ys, zs, color=_accent)
        ax.scatter(xs[1], ys[1], zs[1], s=5, color=_accent)
        ax.text(xs[1] * 1.15, ys[1] * 1.15, zs[1] * 1.15, "|ψ⟩", color=_text)

        plt.tight_layout()
        plt.axis('off')  # removes 3d grid around sphere
        # saves Bloch Sphere as a file and/or shows it as a figure
        if save:
            plt.savefig(path)
        if show:
            plt.show()
