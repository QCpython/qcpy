from .QuantumGateDraw import *
from . import GateFormatting

class CircuitDrawing:
    def __init__(self, circuit):

        self._size = circuit.circuitSize()
        self._queue = circuit.circuitQueue()
        self._drawing = [[EmptySegment() for _ in range(self._size)]]

        for i in self._queue:
            if (self._drawing[len(self._drawing) - 1][i[1]] == EmptySegment()):
                self._drawing[len(self._drawing) - 1][i[1]] = DrawSingleGate(i[0])
            else:
                self._drawing.append([EmptySegment() for _ in range(self._size)])
                self._drawing[len(self._drawing) - 1][i[1]] = DrawSingleGate(i[0])

    def __str__(self):
        res = ''
        for i in range(len(self._drawing[0])):
            res += "q[" + str(i) + "] " + str(EmptySegment())
            for j in range(len(self._drawing)):
                if self._drawing[j][i] != EmptySegment():
                    res += " " + str(self._drawing[j][i]) + " " + str(EmptySegment())
                else:
                    res += str(EmptySegment()) * 3
            res += "\n"
        return res