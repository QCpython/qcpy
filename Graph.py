import matplotlib.pyplot as plt
import numpy as np
import math


class Graph:
    #public
    def __init__(self, qubits):
        """
        """
        self._size = len(qubits)
        self._qubits = qubits
        self.getQubitValues()
        self.getPercents()

    def getQubitValues(self):
        """
        """
        if (self._size % 2 != 0):
            print("QCpy: A critical error has occured and the occuring size of final qubit is: " + str(self._size))
            exit(1)
        for i in range(self._size):
            placeBin = str(bin(i))
            placeBin = placeBin[2:]
            placeBin = (round((math.log(self._size)) + 1 - len(placeBin))*'0') + placeBin
            self._qubitValues.append(placeBin)      

    def getPercents(self):
        """
        """
        total = 0
        for i in range(self._size):
            self._percents.append(100 * self._qubits[i][0])
            total += self._qubits[i][0]
        if 1 < total:
            print("QCpy: A critical error has occured and the calculation is above 100%")
            exit(1)
        
    def makeGraph(self):
        """
        """
        graph = plt.figure()
        ax = plt.axes()
        ax.set_ylim(0, 100)
        ax.bar(self._qubitValues, self._percents)
        plt.xlabel('Computational basis states')
        plt.ylabel('Probability (%)')
        plt.title('Probabilities')
        plt.show()
    #private
    #is the size of the array which will be then converted to the qubit values
    _size = 0
    #array of strings to determine the value of the qubit based off of size
    _qubitValues = []
    #percantages
    _percents = []
    # called in qubit values
    _qubits = []


def main():
    test = Graph([ [.25], [0], [0], [.25], [0], [0], [0], [0], [.0], [.25], [.25], [0], [0], [0], [0], [0] ])
    test.makeGraph()

if __name__ == "__main__":
    main()

    