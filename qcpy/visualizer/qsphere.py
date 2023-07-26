import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from collections import deque
from .tools.sphere import sphere
from ..core.tools import amplitude, phaseangle, probabilities

class qsphere:
    """
    Visualizes the quantum circuit as a q-sphere

    Methods
    --------
    make() :
        returns a Q-Sphere that plots a global visualization of the quantum 
        states in a 3D global view
    """

    def __init__(self, circuit=None):
        """
        Args:
            circuit:
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
                the array of probabilities turned into an array of values adding 
                to 100
            _amplitudes :
                an array of the amplitude for every state
            _phase_angles :
                an array of the phase angle for every state
            _prob_dict :
                a dictionary of the probabilities mapped to the state list
            _phase_dict :
                a dictionary of the phase angles mapped to the state list
            _lat_vals :
                a list of lists of the qubit states in order as the appear upon 
                the latitudes of a QSphere
        """
        self._num_qubits = int(np.log2(len(circuit.probabilities())))
        self._state_list = [
            format(i, 'b').zfill(self._num_qubits)
            for i in range(2**self._num_qubits)
        ]
        self._probabilities = circuit.probabilities()
        self._percents = [i * 100 for i in self._probabilities]
        self._amplitutes = circuit.amplitude().flatten()
        self._phase_angles = circuit.phaseangle().flatten()
        self._prob_dict = {
            self._state_list[i]: self._probabilities[i]
            for i in range(len(self._state_list))
        }
        self._phase_dict = {
            self._state_list[i]: self._phase_angles[i]
            for i in range(len(self._state_list))
        }
        self._lat_vals = self.__latitude_finder__()

    def __hamming_distance__(self, l1: str, l2: str):
        """
        Determines if the count of the number of 1 values match up between
            two strings.

        Args:
            l1: string
            l2: string
        Returns:
            Boolean representation if the count of ones in l1 and l2 are equal 
            to each other.
        """
        return l1.count("1") == l2.count("1")

    def __latitude_finder__(self):
        """
        Creates a 2D array of placed values on each latitude ring, alongside the 
        amount of rotations around the specific lognitude that need to shifted 
        for proper placement.
        Args:
            None
        Returns:
            2D array of needed values and an abstract view of the rotation 
            around each longitude placement, given the length of each row within 
            the 2D array.
        """
        # Main holder of values of latitude placement values
        latitude_values = [[]]
        # will create a 2d array of empty arrays based on the number of qubits
        # - 1, for the starting empty array.
        for _ in range(self._num_qubits - 1):
            latitude_values.append([])
        latitude_values.append([])
        # queue of the given state list from the class object to iterate
        # through each value and then pop them once they are placed in the 2D
        # array
        queue_of_state = deque(self._state_list)
        # base popping of values of 00...0, and 11...1
        latitude_values[0].append(queue_of_state.popleft())
        latitude_values[-1].append(queue_of_state.pop())
        # string value for 0...01 based off of how many qubits there are.
        bit_representation = "0" * (self._num_qubits - 1) + "1"
        # within the range of 1 and the length of the string representing 0...01 and then adding it to
        # each row, while having each index of the string's value to replace a
        # 0 with a one.
        for i in range(1, len(bit_representation)):
            # Add value to main latitude 2d array
            latitude_values[i].append(bit_representation)
            # Get rid of where the string value is located in the queue.
            queue_of_state.remove(bit_representation)
            # creates new string with an extra one in it from the previous
            # iteration.
            list_temp = list(bit_representation)
            list_temp[i - 1] = "1"
            bit_representation = "".join(list_temp)
        # While the queue is not empty, find where each bit representation finds a matching hamming distance with the starting values
        # and store it in the specfic row of the 2D array.
        while queue_of_state:
            # pops the value on the left side of the queue.
            bit_representation = queue_of_state.popleft()
            # goes through the 2d array rows and determines which starting
            # value has the same hamming distance as the bit_representation.
            for i in range(1, len(latitude_values) - 1):
                if (self.__hamming_distance__(
                        bit_representation, latitude_values[i][0])):
                    latitude_values[i].append(bit_representation)

        return latitude_values

    def __getCoords__(self):
        """
        Creates a 2d array of coordinates for the QSphere based off rotation around the latitude, longitude and what values on each segment in proper notation.
        Args:
            None
        Returns:
            A 2D array for coordinates on the QSphere.
        """
        # make lists for coordinates, phi vals, and theta vals
        coords = []
        phi = []
        theta = []

        # gets theta vals
        for i in range(len(self._lat_vals)):
            temp_arr = (
                np.linspace(2 * (np.pi) / len(self._lat_vals[i]),
                            2 * (np.pi), len(self._lat_vals[i]))
            )
            theta.append(temp_arr)

        # gets phi vals
        phi = np.linspace(0, np.pi, self._num_qubits + 1)

        # gets x, y, z coordinate values for lines from center of the QSphere
        # to the surface
        for i in range(len(phi)):
            for j in range(len(theta[i])):
                x1 = 1 * np.sin(phi[i]) * np.cos(theta[i][j])
                y1 = 1 * np.sin(phi[i]) * np.sin(theta[i][j])
                z1 = 1 * np.cos(phi[i])
                x, y, z = [0, x1], [0, y1], [0, z1]
                coords.append([x, y, z])

        return coords

    def make(
            self,
            path: str = "qsphere.png",
            save: bool = False,
            show: bool = True,
            darkmode: bool = True):
        """
            Creates a sphere that visualizes the qubits phase angles if their probability of being measured is greater than 0
        Args:
            path (str): name of the image to be saved
            save (bool): pass True for the graph to be saved
            show (bool): pass True for the sphere to be shown instead of saved
            darkmode (bool): pass True for darkmode, false for lightmode
        """

        if darkmode:
            _text = 'white'
            _accent = '#39c0ba'
            _background = '#2e3037'
        else:
            _text = 'black'
            _accent = 'black'
            _background = 'white'
        ax = sphere(_background)
        # coords will be in the order of states from the __latitude_finder__ function
        # and not in order of self._state_list, we can use our dict to look up each states
        # probability in any order now b/c we do not want to plot a qubit if it
        # has a probability of 0
        coords = self.__getCoords__()
        # turns self._lat_vals into a single list instead of a list of lists
        ham_states = [item for sublist in self._lat_vals for item in sublist]
        # sets up colors that will map to each states phase angle
        colors = plt.get_cmap('hsv')
        norm = plt.Normalize(0, np.pi * 2)

        # function to plot lines from center of the sphere to the surface
        # and qubit states in ket notation, line colors will be basedupon the states
        # phase angle
        for i, j in zip(coords, ham_states):
            cur_prob = self._prob_dict[j]
            cur_phase = self._phase_dict[j]
            # only plot states that have a probability greater than 0
            if cur_prob > 0:
                x, y, z = i[0], i[1], i[2]
                ax.plot3D(x, y, z, color=colors(norm(cur_phase)))
                ax.scatter(
                    x[1], y[1], z[1], s=5,
                    color=colors(norm(cur_phase))
                )
                ax.text(
                    x[1] * 1.15, y[1] * 1.15, z[1] * 1.15,
                    f"|{j}>", color=_text
                )
        # code for colorbar on rightside
        cbar = plt.colorbar(ScalarMappable(cmap=colors, norm=norm), shrink=.55)
        cbar.set_label("Phase Angle", rotation=270, labelpad=15, color=_accent)
        cbar.set_ticks([2 * np.pi, (3 * np.pi) / 2, np.pi, np.pi / 2, 0])
        cbar.ax.yaxis.set_tick_params(color=_text)
        cbar.outline.set_edgecolor(_text)
        cbar.set_ticklabels(["2π", "3π / 2", "π", "π / 2", "0"], color=_text)
        plt.tight_layout()

        plt.axis('off')  # removes 3d grid around sphere
        # saves QSphere as a file and/or shows it as a figure
        if save:
            plt.savefig(path)
        if show:
            plt.show()
