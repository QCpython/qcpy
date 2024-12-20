from typing import List

from .drawings import (
    block_bottom,
    block_connect,
    block_gate,
    block_top,
    horizontal_line,
    multi_connect,
    multi_control,
    single_gate,
    swap_point,
)
from .wire import Wire


class CircuitDrawing:
    """Private handler of generating the circuit drawing.

    Note:
        This is a work in progress and may see some small bugs/invalid formations.
        In other iterations, this will change functionality!

    Args:
        qubits (int): number of qubits.

    Attributes:
        qubits (int): Number of qubits from quantum circuit.
        circuit_queue (arr): 2D-Queue of strings that format/generate the circuit drawing.
        max_length (int): Value to compare when needing to extend rows to match lengths.
    """

    def __init__(self, qubits: int):
        self.qubits = qubits
        self.circuit_queue = []
        self.max_length = 0
        for _ in range(qubits):
            self.circuit_queue.append(Wire())

    def equal_length(self) -> None:
        """Determines and sets all rows of strings to be equal after a gate insertion"""
        for i in range(self.qubits):
            while self.circuit_queue[i].length < self.max_length:
                self.add_drawing(horizontal_line(), i)

    def add_drawing(self, drawing: str, qubit: int) -> None:
        """Inserts drawing at specific qubit drawing row.

        Args:
            drawing (str): number of qubits.
            qubit (int): Which qubit the drawing is inserted at.
        """
        self.circuit_queue[qubit].add(drawing)
        self.max_length = max(self.max_length, self.circuit_queue[qubit].length)

    def insert_single(self, gate: str, qubit: int) -> None:
        """Inserts a single gate drawing into a specific qubit row.

        Note:
            This is a work in progress and may see some small bugs/invalid formations.
            In other iterations, this will change functionality!

        Args:
            qubits (int): number of qubits.

        Attributes:
            qubits (int): Number of qubits from quantum circuit.
            circuit_queue (arr): 2D-Queue of strings that format/generate the circuit drawing.
            max_length (int): Value to compare when needing to extend rows to match lengths.

        """
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

    def two_qubit(self, qubit_1: int, qubit_2: int, gate: str = "") -> None:
        """Adds a two qubit gate into the circuit drawing.
        Args:
            qubit_1 (int): start of range of two qubits.
            qubit_2 (int): end of range of two qubits.
            gate (str): The gate's symbol to be drawn.
        """
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

    def add_multi(self, gate: str, controls: List[int], target: int) -> None:
        """Adds a multi gate drawing (toffoli for example)
        Args:
            gate (str): Character symbol of the gate that is being inserted.
            controls (arr): array of controls on the gate.
            target (int): Where the gate drawing will be inserted.
        """
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
        """Draws a swap gate on a circuit drawing.
        Args:
            qubit_2 (int): first qubit to add 'x' drawing.
            qubit_1 (int): second qubit to add 'x' drawing.
        """
        self.two_qubit(qubit_1=qubit_1, qubit_2=qubit_2)

    def add_control(self, gate: str, control: int, target: int) -> None:
        """Adds a gate that has a singular controlled qubit to the drawing.
        Args:
            gate (str): Character symbol for the target drawing.
            control (int): Control qubit.
            target (int): Target qubit.
        """
        self.two_qubit(qubit_1=control, qubit_2=target, gate=gate)

    def add_block(self, gate: str, qubits: List[int]) -> None:
        """Adds a block drawing to the circuit drawing (example: RC3X).
        Args:
            gate (str): String that represents the gate.
            qubits (int): Which qubits to know the range of the gate.
        """
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

    def make_wire(self, wire: List[str], i: int) -> str:
        """Creates an entire row drawing to print for a singular qubit.

        Args:
            wire (arr): Array of strings to concatenate together.
            i (int): Which qubit is being drawn.
        Returns:
            str: Returns a string of the generated qubit row.

        """
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
        """Generates the entirety of the string to print.
        Returns:
            str: Combination of all qubit strings in a single string.
        """
        output = ""
        for i in range(len(self.circuit_queue)):
            output += self.make_wire(self.circuit_queue[i].content, i)
        return output
