import numpy as np
from ..QuantumCircuit import QuantumCircuit
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

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