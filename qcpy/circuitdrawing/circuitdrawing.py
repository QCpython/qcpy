from . import gateformatting
from .quantumgatedraw import *


class CircuitDrawing:
    def __init__(self, circuit):
        self._size = circuit.circuitSize()
        self._queue = circuit.circuitQueue()
        self._drawing = [[EmptySegment() for _ in range(self._size)]]

        for i in self._queue:
            if self._drawing[len(self._drawing) - 1][i[1]] == EmptySegment():
                self._drawing[len(self._drawing) - 1][i[1]] = DrawSingleGate(i[0])
            else:
                self._drawing.append([EmptySegment() for _ in range(self._size)])
                self._drawing[len(self._drawing) - 1][i[1]] = DrawSingleGate(i[0])

        def __multi_qubit_handeler__(self):
            print(1)

    def __str__(self):
        res = ""
        max_length = 0
        for i in range(len(self._drawing[0])):
            res += "q[" + str(i) + "] " + str(EmptySegment())
            to_output_temp = ""
            for j in range(len(self._drawing)):
                if self._drawing[j][i] != EmptySegment():
                    to_output_temp += (
                        " " + str(self._drawing[j][i]) + (" " * (len(str(self._drawing[j][i])))) + str(EmptySegment())
                    )
                else:
                    to_output_temp += str(EmptySegment()) * 2
            max_length = max(len(to_output_temp), max_length)
            res += to_output_temp + (str(EmptySegment()) * (max_length - len(to_output_temp))) + "\n"
        return res
