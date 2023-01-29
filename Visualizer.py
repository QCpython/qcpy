"""
Visualizer.py

A collection of classes to visualize the quantum circuit

BlochSphere : visualizes the quantum state of a single qubit as a sphere
QSphere : global view of the quantum circuit visualized as a sphere
Statevector : the amplitudes of the quantum circuit visualized as a graph 
Probabilities : the probabilities of each state being measured visualized as a graph
"""
import numpy as np
from .QuantumCircuit import QuantumCircuit
import matplotlib.pyplot as plt
# ScalerMappable is needed for creating the color bar on the State Vector visualization
# that shows what each qubit's phase angle is
from matplotlib.cm import ScalarMappable
# deque is needed for the function that gets the qubit states in order of which the appear
# on a QSphere
from collections import deque

class BlochSphere:
    """
    Visualizes the quantum state of a single qubit as a sphere
    
    Methods
    --------
    makeSphere():
        returns a Bloch Sphere that plots the quantum state of a single qubit in a 
        3D global view
    """
    
    def __init__(self, circuit = None, blochQubit = None):
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
        self._amplitutes = circuit.amplitude().flatten()
        self._phase_angles = circuit.phaseAngle().flatten()
        
    def makeSphere(self, path: str = "BlochSphere.png", save: bool = True, show: bool = False, darkmode: bool = True):
        """
            Creates a sphere of the circuit's probabilties
        Args:
            path (str): name of the image to be saved
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
        plt.clf()
        plt.close()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")     
        u = np.linspace(0,2*np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        r = 1
        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        # wireframe sets up lines around the sphere
        ax.plot_wireframe(x, y, z, rstride = 20, cstride = 20, linewidth=.5, color="lightgray")
        # surface helps give the sphere a translucent look 
        ax.plot_surface(x, y, z,  color="linen", alpha=.1)
        ax.scatter(0,0,0, s=5, color="black")
        # plots accent lines around the sphere
        theta = np.linspace(0, 2 * np.pi, 100)
        zs = np.zeros(100)
        xs = r * np.sin(theta)
        ys = r * np.cos(theta)
        ax.plot(xs, ys, zs, color='black', alpha=0.25) # line around equator
        ax.plot(zs, xs, ys, color='black', alpha=0.25) # line around north & south poles
        # accent lines along x, y, and z axes
        zeros = np.zeros(100)
        line = np.linspace(-1,1,100)
        ax.plot(line, zeros, zeros, color='black', alpha=0.25)
        ax.plot(zeros, line, zeros, color='black', alpha=0.25)
        ax.plot(zeros, zeros, line, color='black', alpha=0.25)
        # sets backgorund color
        ax.set_facecolor(_background)
        fig.patch.set_facecolor(_background)
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
        
        ### For testing purposes only now
        zero = np.array([[
            1+0j,
            0+0j
        ]])

        one = np.array([[
            0+0j,
            1+0j
        ]])
        
        final = np.array([])
        
        for i in range(len(self._phase_angles)):
            theta = self._amplitutes[i]
            phi = self._phase_angles[i]
            placement = np.cos(theta / 2) * zero + (np.exp(0+1j * phi) * np.sin(theta / 2) * one)
            final = np.append(final, placement)
        z = final[1::2].flatten()
        y = final[::2].flatten()
        z = z[0]
        y = y[0]

        # gets x, y, z cartesian coords
        x1 = 1 * np.sin(phi) * np.cos(theta)
        y1 = 1 * np.sin(phi) * np.sin(theta)
        z1 = 1 * np.cos(phi)
        # plots a line from center to surface
        xs, ys, zs = [0, x1], [0, y1], [0, z1]
        ax.plot3D(xs, ys, zs, color=_accent)
        ax.scatter(xs[1], ys[1], zs[1], s=5, color=_accent)
        ax.text(xs[1] * 1.15, ys[1] * 1.15, zs[1] * 1.15, "|ψ⟩", color=_text)
        
        plt.axis('off') # removes 3d grid around sphere
        # saves Bloch Sphere as a file and/or shows it as a figure
        if save:
            plt.savefig(path)
        if show:
            plt.show()

class QSphere:
    """
    Visualizes the quantum circuit as a q-sphere
   
    Methods
    --------
    makeSphere() :
        returns a Q-Sphere that plots a global visualization of the quantum states
        in a 3D global view
    """

    def __init__(self, circuit = None):
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
                the array of probabilities turned into an array of values adding to 100
            _amplitudes :
                an array of the amplitude for every state
            _phase_angles :
                an array of the phase angle for every state
            _prob_dict :
                a dictionary of the probabilities mapped to the state list
            _phase_dict :
                a dictionary of the phase angles mapped to the state list
            _lat_vals :
                a list of lists of the qubit states in order as the appear upon the latitudes of a QSphere
        """
        self._num_qubits =  int(np.log2(len(circuit.probabilities())))
        self._state_list = [format(i, 'b').zfill(self._num_qubits) for i in range(2**self._num_qubits)]
        self._probabilities = circuit.probabilities()
        self._percents = [i * 100 for i in self._probabilities]
        self._amplitutes = circuit.amplitude().flatten()
        self._phase_angles = circuit.phaseAngle().flatten()
        self._prob_dict = {self._state_list[i]: self._probabilities[i] for i in range(len(self._state_list))}
        self._phase_dict = {self._state_list[i]: self._phase_angles[i] for i in range(len(self._state_list))}
        self._lat_vals = self.__latitude_finder__()
                
    def __hamming_distance__(self, l1: str, l2: str):
        """
        Determines if the count of the number of 1 values match up between two strings.

        Args:
            l1: string
            l2: string
        Returns:
            Boolean representation if the count of ones in l1 and l2 are equal to each other.
        """
        return l1.count("1") == l2.count("1")
    
    def __latitude_finder__(self):
        """
        Creates a 2D array of placed values on each latitude ring, alongside the amount of rotations around the specific lognitude that need to shifted for proper placement.
        Args:
            None
        Returns:
            2D array of needed values and an abstract view of the rotation around each longitude placement, given the length of each row within the 2D array.
        """
        # Main holder of values of latitude placement values
        latitude_values = [[]]
        # will create a 2d array of empty arrays based on the number of qubits - 1, for the starting empty array.
        for _ in range(self._num_qubits - 1):
            latitude_values.append([])
        latitude_values.append([])
        # queue of the given state list from the class object to iterate through each value and then pop them once they are placed in the 2D array
        queue_of_state = deque(self._state_list)
        # base popping of values of 00...0, and 11...1
        latitude_values[0].append(queue_of_state.popleft())
        latitude_values[-1].append(queue_of_state.pop())
        # string value for 0...01 based off of how many qubits there are.
        bit_representation = "0" * (self._num_qubits - 1) + "1"
        # within the range of 1 and the length of the string representing 0...01 and then adding it to
        # each row, while having each index of the string's value to replace a 0 with a one.
        for i in range(1, len(bit_representation)):
            # Add value to main latitude 2d array
            latitude_values[i].append(bit_representation)
            # Get rid of where the string value is located in the queue.
            queue_of_state.remove(bit_representation)
            # creates new string with an extra one in it from the previous iteration.
            list_temp = list(bit_representation)
            list_temp[i - 1] = "1"
            bit_representation = "".join(list_temp)
        # While the queue is not empty, find where each bit representation finds a matching hamming distance with the starting values
        # and store it in the specfic row of the 2D array.
        while queue_of_state:
            # pops the value on the left side of the queue.
            bit_representation = queue_of_state.popleft()
            # goes through the 2d array rows and determines which starting value has the same hamming distance as the bit_representation.
            for i in range(1, len(latitude_values) - 1):
                if (self.__hamming_distance__(bit_representation, latitude_values[i][0])):
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
            temp_arr = (np.linspace(2*(np.pi)/len(self._lat_vals[i]), 2*(np.pi), len(self._lat_vals[i])))
            theta.append(temp_arr)
        
        # gets phi vals
        phi = np.linspace(0, np.pi, self._num_qubits + 1) 
            
        # gets x, y, z coordinate values for lines from center of the QSphere to the surface    
        for i in range(len(phi)):
            for j in range(len(theta[i])):
                x1 = 1 * np.sin(phi[i]) * np.cos(theta[i][j])
                y1 = 1 * np.sin(phi[i]) * np.sin(theta[i][j])
                z1 = 1 * np.cos(phi[i])
                x, y, z = [0, x1], [0, y1], [0, z1]
                coords.append([x, y, z])
        
        return coords
    
    def makeSphere(self, path: str = "qsphere.png", save: bool = True, show: bool = False, darkmode: bool = True):
        """
            Creates a sphere of the circuit's probabilties
        Args:
            path (str): name of the image to be saved
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
        plt.clf()
        plt.close()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")     
        u = np.linspace(0,2*np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        r = 1
        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        # wireframe sets up lines around the sphere
        ax.plot_wireframe(x, y, z, rstride = 20, cstride = 20, linewidth=.5, color="lightgray")
        # surface helps give the sphere a translucent look 
        ax.plot_surface(x, y, z,  color="linen", alpha=.1)
        ax.scatter(0,0,0, s=5, color="black")
        # plots accent lines around the sphere
        theta = np.linspace(0, 2 * np.pi, 100)
        zs = np.zeros(100)
        xs = r * np.sin(theta)
        ys = r * np.cos(theta)
        ax.plot(xs, ys, zs, color='black', alpha=0.25) # line around equator
        ax.plot(zs, xs, ys, color='black', alpha=0.25) # line around north & south poles
        # accent lines along x, y, and z axes
        zeros = np.zeros(100)
        line = np.linspace(-1,1,100)
        ax.plot(line, zeros, zeros, color='black', alpha=0.25)
        ax.plot(zeros, line, zeros, color='black', alpha=0.25)
        ax.plot(zeros, zeros, line, color='black', alpha=0.25)
        
        # coords will be in the order of states from the __latitude_finder__ function
        # and not in order of self._state_list, we can use our dict to look up each states
        # probability in any order now b/c we do not want to plot a qubit if it has a probability of 0
        coords = self.__getCoords__()
        # turns self._lat_vals into a single list instead of a list of lists
        ham_states = [item for sublist in self._lat_vals for item in sublist]  
        # sets up colors that will map to each states phase angle
        colors = plt.get_cmap('hsv')
        norm = plt.Normalize(0, np.pi*2)
        
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
                ax.scatter(x[1], y[1], z[1], s=5, color=colors(norm(cur_phase)))
                ax.text(x[1] * 1.15, y[1] * 1.15, z[1] * 1.15, f"|{j}>", color=_text)
                
        # sets backgorund color
        ax.set_facecolor(_background)
        fig.patch.set_facecolor(_background)
        # code for colorbar on rightside
        cbar = plt.colorbar(ScalarMappable(cmap=colors, norm=norm), shrink=.55)
        cbar.set_label("Phase Angle", rotation=270, labelpad=15, color=_accent)
        cbar.set_ticks([2*np.pi, (3*np.pi)/2, np.pi, np.pi/2, 0])
        cbar.ax.yaxis.set_tick_params(color=_text)
        cbar.outline.set_edgecolor(_text)
        cbar.set_ticklabels(["2π", "3π / 2", "π", "π / 2", "0"], color=_text)
        plt.tight_layout()
        
        plt.axis('off') # removes 3d grid around sphere
        # saves QSphere as a file and/or shows it as a figure
        if save:
            plt.savefig(path)
        if show:
            plt.show()
    
class StateVector:
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
        self._num_qubits =  int(np.log2(len(circuit.probabilities())))
        self._state_list = [format(i, 'b').zfill(self._num_qubits) for i in range(2**self._num_qubits)]
        self._probabilities = circuit.probabilities()
        self._percents = [i * 100 for i in circuit.probabilities()]
        self._amplitutes = circuit.amplitude().flatten()
        self._phase_angles = circuit.phaseAngle().flatten()
        
    def makeGraph(self, path: str = "statevector.png", save: bool = True, show: bool = False, darkmode: bool = True):
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
            _text = 'white'
            _accent = '#39c0ba'
            _background = '#2e3037'
        else:
            _text = 'black'
            _accent = 'black'
            _background = 'white'
        
        # clears any previous plots    
        plt.clf()
        plt.close()
        # sets up bar graph and colors that map to a qubits phase angle
        fig, ax = plt.subplots(figsize=(self._num_qubits + 3, self._num_qubits + 3))
        colors = plt.get_cmap('hsv')
        norm = plt.Normalize(0, np.pi*2)
        ax.bar(self._state_list, self._amplitutes, color=colors(norm(self._phase_angles)))
        # sets up tick labels
        plt.setp(ax.get_xticklabels(), rotation=75, ha='right', color=_text)
        plt.setp(ax.get_yticklabels(), color=_text)
        # cleans outline of bargraph so it's open to the top and right
        ax.spines['bottom'].set_color(_text)
        ax.spines['top'].set_color(_background) 
        ax.spines['right'].set_color(_background)
        ax.spines['left'].set_color(_text)
        # sets up tick parameters
        ax.tick_params(axis='x', colors=_text)
        ax.tick_params(axis='y', colors=_text)
        ax.set_ylim(0, np.amax(self._amplitutes))
        # sets backgorund color
        ax.set_facecolor(_background)
        fig.patch.set_facecolor(_background)
        # sets x and y labels and title
        plt.xlabel('Computational basis states', color=_accent)
        plt.ylabel('Amplitutde', labelpad=5, color=_accent)
        plt.title('State Vector', pad=10, color=_accent)
        # code for colorbar on rightside 
        cbar = plt.colorbar(ScalarMappable(cmap=colors, norm=norm))
        cbar.set_label("Phase Angle", rotation=270, labelpad=10, color=_accent)
        cbar.set_ticks([2*np.pi, (3*np.pi)/2, np.pi, np.pi/2, 0])
        cbar.ax.yaxis.set_tick_params(color=_text)
        cbar.outline.set_edgecolor(_text)
        cbar.set_ticklabels(["2π", "3π / 2", "π", "π / 2", "0"], color=_text)
        plt.tight_layout()
        
        # saves State Vector as a file and/or shows it as a figure
        if save:
            plt.savefig(path)
        if show:
            plt.show()
                     
class Probabilities:
    """
    Visualizes the quantum circuit's qubits probability of being measured using a bar graph
   
    Methods
    --------
    makeGraph(path: str, show: bool) :
        returns a graph that plots all the probabilities of the qubits being measured
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
            _percents :
                the array of probabilities turned into an array of values adding to 100
        """
        self._num_qubits =  int(np.log2(len(circuit.probabilities())))
        self._state_list = [format(i, 'b').zfill(self._num_qubits) for i in range(2**self._num_qubits)]
        self._percents = [i * 100 for i in circuit.probabilities()]
            
    def makeGraph(self, path: str = "probabilities.png", save: bool = True, show: bool = False, darkmode: bool = True):
        """
            Creates a graph of the circuit's probabilties
        Args:
            path (str): name of the image to be saved
            save (bool): pass True for the graph to be saved 
            show (bool): pass True for the graph to be shown
            darkmode (bool): pass True for darkmode and false for lightmode
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
        
        # clears any previous plots
        plt.clf()
        plt.close()
        # sets up bar graph
        fig, ax = plt.subplots(figsize=(self._num_qubits + 3, self._num_qubits + 3))
        ax.bar(self._state_list, self._percents, color='#39c0ba')
        # sets range of ticks on y-axis
        plt.yticks(np.arange(0, 110, 10))
        # sets up tick labels
        plt.setp(ax.get_xticklabels(), rotation=75, ha='right', color=_text)
        plt.setp(ax.get_yticklabels(), color=_text)
        # cleans outline of bargraph so its open to the top and right
        ax.spines['bottom'].set_color(_text)
        ax.spines['top'].set_color(_background) 
        ax.spines['right'].set_color(_background)
        ax.spines['left'].set_color(_text)
        # sets up tick parameters
        ax.tick_params(axis='x', colors=_text)
        ax.tick_params(axis='y', colors=_text)
        ax.set_ylim(0, 100)
        # sets backgorund color
        ax.set_facecolor(_background)
        fig.patch.set_facecolor(_background)
        # sets x and y labels and title
        plt.xlabel('Computational basis states', color=_accent)
        plt.ylabel('Probability (%)', labelpad=5, color=_accent)
        plt.title('Probabilities', pad=10, color=_accent)
        plt.tight_layout()
        
        # saves Probabilties as a file and/or shows it as a figure
        if save:
            plt.savefig(path)
        if show:
            plt.show()
            
