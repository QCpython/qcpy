from .drawings import *
from .wire import Wire


class CircuitDrawing:
    def __init__(self, qubits: int):
        self.qubits = qubits
        self.circuit_queue = []
        self.max_length = 0
        for _ in range(qubits):
            self.circuit_queue.append(Wire())

    def equal_length(self) -> None:
        for i in range(self.qubits):
            while self.circuit_queue[i].length < self.max_length:
                self.add_drawing(horizontal_line(), i)

    def add_drawing(self, drawing: str, qubit: int) -> None:
        self.circuit_queue[qubit].add(drawing)
        self.max_length = max(self.max_length, self.circuit_queue[qubit].length)

    def insert_single(self, gate: str, qubit: int) -> None:
        to_insert = self.max_length - 1
        if self.max_length:
            while (
                to_insert > 0
                and self.circuit_queue[qubit].at(to_insert) == horizontal_line()
            ):
                to_insert -= 1
            if self.circuit_queue[qubit].at(to_insert) != horizontal_line():
                to_insert += 1
            self.circuit_queue[qubit].insert(to_insert, single_gate(gate))
            self.max_length = max(self.max_length, self.circuit_queue[qubit].length)
        else:
            self.add_drawing(single_gate(gate), qubit)
        self.equal_length()

    def two_qubit(self, qubit_1: int, qubit_2: int, gate=None) -> None:
        self.equal_length()
        start = min(qubit_1, qubit_2)
        end = max(qubit_1, qubit_2)
        for i in range(start + 1, end):
            self.add_drawing(multi_connect(), i)
        if gate:
            self.add_drawing(multi_control(is_end=qubit_1 > qubit_2), qubit_1)
            self.add_drawing(
                single_gate(gate, is_controlled=True, is_start=qubit_1 > qubit_2),
                qubit_2,
            )
        else:
            self.add_drawing(swap_point(), qubit_1)
            self.add_drawing(swap_point(), qubit_2)
        self.equal_length()

    def add_multi(self, gate: str, controls, target: int) -> None:
        controls.append(target)
        self.equal_length()
        for i in range(self.qubits):
            if i == target:
                if target <= min(controls):
                    self.add_drawing(
                        single_gate(gate, is_controlled=True, is_start=True), i
                    )
                else:
                    self.add_drawing(single_gate(gate, is_controlled=True), i)
            elif min(controls) == i:
                self.add_drawing(multi_control(), i)
            elif max(controls) == i:
                self.add_drawing(multi_control(is_end=True), i)
            elif i in controls:
                self.add_drawing(multi_control(is_connector=True), i)
            elif i in range(min(controls), max(controls)):
                self.add_drawing(multi_connect(), i)
        self.equal_length()

    def add_swap(self, qubit_1, qubit_2) -> None:
        self.two_qubit(qubit_1=qubit_1, qubit_2=qubit_2)

    def add_control(self, gate, control, target) -> None:
        self.two_qubit(qubit_1=control, qubit_2=target, gate=gate)

    def add_block(self, gate: str, qubits) -> None:
        center = (max(qubits) + min(qubits)) // 2
        for i in range(self.qubits):
            if i == center:
                self.add_drawing(block_gate(gate), i)
            elif i == min(qubits):
                self.add_drawing(block_top(), i)
            elif i == max(qubits):
                self.add_drawing(block_bottom(), i)
            elif i in range(min(qubits), max(qubits)) or i in qubits:
                self.add_drawing(block_connect(), i)
        self.equal_length()

    def make_wire(self, wire, i) -> str:
        top = ["   "]
        middle = ["q" + str(i) + "─"]
        bottom = ["   "]
        if self.qubits >= 10:
            top += "  "
            middle += "─" if i >= 10 else "──"
            bottom += "  "
        for item in range(len(wire)):
            size = len(wire[item]) // 3
            for counter in range(size):
                top[-1] += wire[item][counter]
                middle[-1] += wire[item][counter + size]
                bottom[-1] += wire[item][counter + size * 2]
        return "".join(top) + "\n" + "".join(middle) + "\n" + "".join(bottom) + "\n"

    def make(self) -> str:
        output = ""
        for i in range(len(self.circuit_queue)):
            output += self.make_wire(self.circuit_queue[i].content, i)
        return output
