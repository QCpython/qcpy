"""
Visualizer.py

A collection of classes to visualize the quantum circuit

QSphere : global view of the quantum circuit visualized as a Sphere
Statevector : the amplitudes of the quantum circuit visualized as a graph and/or sphere
Probabilities : the probabilities of each state being measured visualized as a graph
"""
import numpy as np
from QuantumCircuit import QuantumCircuit
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

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
        """
        self._num_qubits =  int(np.log2(len(circuit.probabilities())))
        self._state_list = [format(i, 'b').zfill(self._num_qubits) for i in range(2**self._num_qubits)]
        self._probabilities = circuit.probabilities()
        self._percents = [i * 100 for i in self._probabilities]
        
    def __hamming_distance__(self, l1 ,l2):
        return sum(ket1 != ket2 for ket1, ket2 in zip(l1, l2))
            
    def __getCoords__(self):
        """ 
        returns an array of x, y, z line coords for all the states
        """
        coords = []
        if self._num_qubits == 1: #base case
            x, y, z = [0, 0], [0, 0], [0, 1]
            coords.append([x, y, z]) #|0>
            z = [0, -1]
            coords.append([x, y, z]) #|1>
        elif self._num_qubits == 2:
            x, y, z = [0, 0], [0, 0], [0, 1] 
            coords.append([x, y, z]) #|00>
            x, z = [0, -1], [0, 0]
            coords.append([x, y, z]) #|01>
            x = [0, 1]
            coords.append([x, y, z]) #|10>
            x, z = [0, 0], [0, -1]
            coords.append([x, y, z]) #|11>

        return coords
    
    def makeSphere(self, path: str = "qsphere.png", save: bool = True, show: bool = False):
        """
            Creates a aphere of the circuit's probabilties
        Args:
            path (str): name of the image to be saved
            save (bool): pass True for the graph to be saved
            show (bool): pass True for the sphere to be shown instead of saved
        """
        plt.clf()
        plt.close()
        ax = plt.axes(projection="3d")
        u = np.linspace(0,2*np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        r = 1
        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_wireframe(x, y, z, rstride = 10, cstride = 10, linewidth=1, color="gray")
        ax.scatter(0,0,0)
        
        coords = self.__getCoords__()
        for i, j, k in zip(self._probabilities, coords, self._state_list):
            if i > 0: # if probability of curent state is greater than 0
                x, y, z = j[0], j[1], j[2]
                ax.plot3D(x, y, z, color="red")
                ax.text(x[1], y[1], z[1], f"|{k}>")
            
        plt.axis('off')
        if save:
            plt.savefig(path)
        if show:
            plt.show()
    
class StateVector:
    """
    Visualizes the quantum circuit's quantum amplitutes using a bar graph and a sphere
   
    Methods
    --------
    makeGraph() :
        returns a graph that plots all the amplitudes of the qubits being measured

    makeSphere() :
        returns a sphere that plots a global visualization of the quantum amplitudes
        in a 3D global view
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
            darkmode (bool): pass True for darkmode
        """
        if darkmode:
            _text = 'white'
            _accent = '#39c0ba'
            _background = '#2e3037'
        else:
            _text = 'black'
            _accent = 'black'
            _background = 'white'
            
        plt.clf()
        plt.close()
        fig, ax = plt.subplots(figsize=(self._num_qubits + 3, self._num_qubits + 3))
        colors = plt.get_cmap('hsv')
        norm = plt.Normalize(0, np.pi*2)
        ax.bar(self._state_list, self._amplitutes, color=colors(norm(self._phase_angles)))
        plt.setp(ax.get_xticklabels(), rotation=75, ha='right', color=_text)
        plt.setp(ax.get_yticklabels(), color=_text)
        ax.spines['bottom'].set_color(_text)
        ax.spines['top'].set_color(_background) 
        ax.spines['right'].set_color(_background)
        ax.spines['left'].set_color(_text)
        ax.tick_params(axis='x', colors=_text)
        ax.tick_params(axis='y', colors=_text)
        ax.set_ylim(0, np.amax(self._amplitutes))
        ax.set_facecolor(_background)
        fig.patch.set_facecolor(_background)
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
        
        if save:
            plt.savefig(path)
        if show:
            plt.show()
            
class Probabilities:
    """
    Visualizes the quantum circuit using a bar graph
   
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
            darkmode (bool): pass True for darkmode
        """
        if darkmode:
            _text = 'white'
            _accent = '#39c0ba'
            _background = '#2e3037'
        else:
            _text = 'black'
            _accent = 'black'
            _background = 'white'
        
        plt.clf()
        plt.close()
        fig, ax = plt.subplots(figsize=(self._num_qubits + 3, self._num_qubits + 3))
        ax.bar(self._state_list, self._percents, color='#39c0ba')
        plt.yticks(np.arange(0, 110, 10))
        plt.setp(ax.get_xticklabels(), rotation=75, ha='right', color=_text)
        plt.setp(ax.get_yticklabels(), color=_text)
        ax.spines['bottom'].set_color(_text)
        ax.spines['top'].set_color(_background) 
        ax.spines['right'].set_color(_background)
        ax.spines['left'].set_color(_text)
        ax.tick_params(axis='x', colors=_text)
        ax.tick_params(axis='y', colors=_text)
        ax.set_facecolor(_background)
        fig.patch.set_facecolor(_background)
        ax.set_ylim(0, 100)
        plt.xlabel('Computational basis states', color=_accent)
        plt.ylabel('Probability (%)', labelpad=5, color=_accent)
        plt.title('Probabilities', pad=10, color=_accent)
        plt.tight_layout()
        
        if save:
            plt.savefig(path)
        if show:
            plt.show()
            
