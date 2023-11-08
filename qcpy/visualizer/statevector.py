import matplotlib.pyplot as plt
import numpy as np

# ScalerMappable is needed for creating the color bar on the State Vector
# visualization
from matplotlib.cm import ScalarMappable
from matplotlib.colors import rgb2hex

from ..core import quantumcircuit
from .tools.graph import graph


class statevector:
    """
    Visualizes the quantum circuit's quantum amplitutes using a bar graph

    Methods
    --------
    makeGraph() :
        returns a graph that plots all the amplitudes of the qubits being measured
    """

    def __init__(self, circuit=None):
        """
        Args:
            circuit :
                the quantum circuit
        ------
        Variables:
            _num_qubits :
                the number of qubits on the circuit
            _state_list :
                all the states of the qubits on the circuit
            _probabilities :
                an array of all the probabilities of the qubits being measured
            _percents :
                the array of probabilities turned into an array of values adding to 100
            _amplitudes :
                an array of the amplitude for every state
            _phase_angles :
                an array of the phase angle for every state
        """
        self._num_qubits = circuit.circuitSize()
        self._state_list = [format(i, "b").zfill(self._num_qubits) for i in range(2**self._num_qubits)]
        self._probabilities = circuit.probabilities()
        self._percents = [i * 100 for i in circuit.probabilities()]
        self._amplitutes = circuit.amplitude().flatten()
        self._phase_angles = circuit.phaseAngle().flatten()

    def make(self, path: str = "statevector.png", save: bool = True, show: bool = False, darkmode: bool = True):
        """
            Creates a graph of the circuit's amplitudes and phase angles
        Args:
            path (str): name of the image to be saved
            save (bool): pass True for the graph to be saved
            show (bool): pass True for the graph to be shown instead of saved
            darkmode (bool): pass True for darkmode and false for lightmode
        """
        # sets up darkmode or lightmode
        if darkmode:
            _text = "white"
            _accent = "#39c0ba"
            _background = "#2e3037"
        else:
            _text = "black"
            _accent = "black"
            _background = "white"

        # clears any previous plots
        ax = graph(_text, _background, self._num_qubits)

        ax.set_ylim(0, np.amax(self._amplitutes))
        colors = plt.get_cmap("hsv")  # color map
        # need phase angle values to be normalized from 0 to 2pi
        norm = plt.Normalize(0, np.pi * 2)
        # array of hexvals corresponding to qubit's phase angles
        hex_arr = [rgb2hex(i) for i in colors(norm(self._phase_angles))]
        ax.bar(self._state_list, self._amplitutes, color=hex_arr)
        # sets x and y labels and title
        plt.xlabel("Computational basis states", color=_accent)
        plt.ylabel("Amplitutde", labelpad=5, color=_accent)
        plt.title("State Vector", pad=10, color=_accent)
        # code for colorbar on rightside
        cbar = plt.colorbar(ScalarMappable(cmap=colors, norm=norm))
        cbar.set_label("Phase Angle", rotation=270, labelpad=10, color=_accent)
        cbar.set_ticks([2 * np.pi, (3 * np.pi) / 2, np.pi, np.pi / 2, 0])
        cbar.ax.yaxis.set_tick_params(color=_text)
        cbar.outline.set_edgecolor(_text)
        cbar.set_ticklabels(["2π", "3π / 2", "π", "π / 2", "0"], color=_text)
        plt.tight_layout()

        # saves State Vector as a file and/or shows it as a figure
        if save:
            plt.savefig(path)
        if show:
            plt.show()
