import numpy as np
from ..QuantumCircuit import QuantumCircuit
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

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