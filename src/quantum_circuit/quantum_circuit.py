import numpy as np
from .base import BaseCalculator
from .sparse import SparseCalculator
from .gpu import GpuCalculator
from .gpu_sparse import GpuSparseCalculator
import subprocess
from ..circuit_drawing import CircuitDrawing
from ..quantum_gate import *
from ..errors import *


class QuantumCircuit:
    def __init__(
        self,
        qubits: int,
        big_endian: bool = False,
        prep: chr = "z",
        sparse: bool = False,
        gpu: bool = False,
    ):
        self.calculator = None
        self.sparse = sparse
        self.gpu = gpu
        if prep != "z" and prep != "y" and prep != "x":
            raise InvalidQubitPrepError("Qubit prep is not x,y,or z")
        if self.gpu:
            try:
                subprocess.check_output(["nvcc", "--version"]).decode()
            except FileNotFoundError:
                self.gpu = False
        if self.sparse and self.gpu:
            self.calculator = GpuSparseCalculator(qubits, big_endian, prep)
        elif self.sparse:
            self.calculator = SparseCalculator(qubits, big_endian, prep)
        elif self.gpu:
            self.calculator = GpuCalculator(qubits, big_endian, prep)
        else:
            self.calculator = BaseCalculator(qubits, big_endian, prep)
        self.circuit_drawing = CircuitDrawing(qubits)

    def __eq__(self, circuit) -> bool:
        temp_state = self.calculator.state
        foreign_temp = circuit.calculator.state
        if self.sparse:
            temp_state = temp_state.toarray()
        if circuit.sparse:
            foreign_temp = foreign_temp.toarray()
        return (temp_state == foreign_temp).all()

    def __str__(self) -> str:
        return self.circuit_drawing.make()

    def __len__(self) -> int:
        return 2**self.calculator.qubits

    def __add_single_drawing__(self, qubits_to_apply, gate: str) -> None:
        if not isinstance(qubits_to_apply, int):
            for qubit in qubits_to_apply:
                if qubit not in range(self.calculator.qubits):
                    OutOfRangeError("qubit is out of range of size of quantum circuit")
                self.circuit_drawing.insert_single(gate, qubit)
        elif isinstance(qubits_to_apply, int):
            if qubits_to_apply not in range(self.calculator.qubits):
                OutOfRangeError("qubit is out of range of size of quantum circuit")
            self.circuit_drawing.insert_single(gate, qubits_to_apply)

    def set(self, circuit) -> None:
        self.calculator.state = circuit.calculator.state

    @property
    def state(self):
        if not self.sparse and not self.gpu:
            temp_state = self.calculator.state
        if self.sparse and self.gpu:
            temp_state = self.calculator.state.get()
            temp_state = np.array(temp_state.toarray(), "F")
        if self.gpu and not self.sparse:
            temp_state = self.calculator.state.get()
        if self.sparse and not self.gpu:
            temp_state = np.array(self.calculator.state.toarray(), "F")
        return temp_state

    @property
    def size(self) -> int:
        return self.calculator.qubits

    def i(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, identity())
        self.__add_single_drawing__(qubits_to_apply, "I")

    def h(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, hadamard())
        self.__add_single_drawing__(qubits_to_apply, "H")

    def x(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, paulix())
        self.__add_single_drawing__(qubits_to_apply, "X")

    def y(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, pauliy())
        self.__add_single_drawing__(qubits_to_apply, "Y")

    def z(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, pauliz())
        self.__add_single_drawing__(qubits_to_apply, "Z")

    def p(self, qubits_to_apply, theta: float = np.pi / 2) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, phase(theta))
        self.__add_single_drawing__(qubits_to_apply, "P")

    def s(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, s())
        self.__add_single_drawing__(qubits_to_apply, "S")

    def sdg(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, sdg())
        self.__add_single_drawing__(qubits_to_apply, "S†")

    def t(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, t())
        self.__add_single_drawing__(qubits_to_apply, "T")

    def tdg(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, tdg())
        self.__add_single_drawing__(qubits_to_apply, "T†")

    def rz(self, qubits_to_apply, theta: float = np.pi / 2) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, rz(theta))
        self.__add_single_drawing__(qubits_to_apply, "RZ")

    def ry(self, qubits_to_apply, theta: float = np.pi / 2) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, ry(theta))
        self.__add_single_drawing__(qubits_to_apply, "RY")

    def rx(self, qubits_to_apply, theta: float = np.pi / 2) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, rx(theta))
        self.__add_single_drawing__(qubits_to_apply, "RX")

    def sx(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, sx())
        self.__add_single_drawing__(qubits_to_apply, "SX")

    def sxdg(self, qubits_to_apply) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, sxdg())
        self.__add_single_drawing__(qubits_to_apply, "SX†")

    def u(
        self,
        qubits_to_apply,
        theta: float = np.pi / 2,
        phi: float = np.pi / 2,
        lmbda: float = np.pi / 2,
    ) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, u(theta, phi, lmbda))
        self.__add_single_drawing__(qubits_to_apply, "U")

    def custom(self, qubits_to_apply, gate: np.array) -> None:
        self.calculator.pass_single_gate(qubits_to_apply, gate)
        self.__add_single_drawing__(qubits_to_apply, "C")

    def gatearray(self, gate_array) -> None:
        self.calculator.pass_custom_gate_queue(gate_array)

    def cx(self, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, paulix())
        self.circuit_drawing.add_control("X", control, target)

    def ch(self, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, hadamard())
        self.circuit_drawing.add_control("H", control, target)

    def cy(self, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, pauliy())
        self.circuit_drawing.add_control("Y", control, target)

    def cz(self, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, pauliz())
        self.circuit_drawing.add_control("Z", control, target)

    def crx(self, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, rx())
        self.circuit_drawing.add_control("RX", control, target)

    def cry(self, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, ry())
        self.circuit_drawing.add_control("RY", control, target)

    def crz(self, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, rz())
        self.circuit_drawing.add_control("RZ", control, target)

    def cr1(self, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, r1())
        self.circuit_drawing.add_control("R1", control, target)

    def multicustom(self, gate: np.array, control: int, target: int) -> None:
        self.calculator.pass_multi_gate(control, target, gate)
        self.circuit_drawing.add_control("C", control, target)

    def ccx(self, control_one: int, control_two: int, target: int) -> None:
        self.calculator.pass_multi_gate(control_two, target, sx())
        self.calculator.pass_multi_gate(control_one, control_two, paulix())
        self.calculator.pass_multi_gate(control_two, target, sxdg())
        self.calculator.pass_multi_gate(control_one, control_two, paulix())
        self.calculator.pass_multi_gate(control_one, target, sx())
        self.circuit_drawing.add_multi("X", [control_one, control_two], target)

    def qft(self, qubit_one: int, qubit_two: int, qubit_three: int) -> None:
        self.calculator.pass_single_gate(qubit_one, hadamard())
        self.calculator.pass_multi_gate(qubit_two, qubit_one, r1())
        self.calculator.pass_multi_gate(qubit_two, qubit_three, r1())
        self.calculator.pass_single_gate(qubit_two, hadamard())
        self.calculator.pass_multi_gate(qubit_three, qubit_two, r1())
        self.calculator.pass_single_gate(qubit_three, hadamard())
        self.calculator.pass_multi_gate(qubit_one, qubit_three, paulix())
        self.calculator.pass_multi_gate(qubit_three, qubit_one, paulix())
        self.calculator.pass_multi_gate(qubit_one, qubit_three, paulix())
        self.circuit_drawing.add_block("QFT", [qubit_one, qubit_two, qubit_three])

    def rccx(self, control_one: int, control_two: int, target: int) -> None:
        self.calculator.pass_single_gate(target, u(np.pi / 2, 0, np.pi))
        self.calculator.pass_single_gate(target, u(0, 0, np.pi / 4))
        self.calculator.pass_multi_gate(control_two, target, paulix())
        self.calculator.pass_single_gate(target, u(0, 0, (-1 * np.pi) / 4))
        self.calculator.pass_multi_gate(control_one, target, paulix())
        self.calculator.pass_single_gate(target, u(0, 0, np.pi / 4))
        self.calculator.pass_multi_gate(control_two, target, paulix())
        self.calculator.pass_single_gate(target, u(0, 0, (-1 * np.pi) / 4))
        self.calculator.pass_single_gate(target, u(np.pi / 2, 0, np.pi))
        self.circuit_drawing.add_block("RCCX", [control_one, control_two, target])

    def rc3x(self, qubit_1: int, qubit_2: int, qubit_3: int, qubit_4: int) -> None:
        self.calculator.pass_single_gate(qubit_4, u(np.pi / 2, 0, np.pi))
        self.calculator.pass_single_gate(qubit_4, u(0, 0, np.pi / 4))
        self.calculator.pass_multi_gate(qubit_3, qubit_4, paulix())
        self.calculator.pass_single_gate(qubit_4, u(0, 0, (-1 * np.pi) / 4))
        self.calculator.pass_single_gate(qubit_4, u(np.pi / 2, 0, np.pi))
        self.calculator.pass_multi_gate(qubit_1, qubit_4, paulix())
        self.calculator.pass_single_gate(qubit_4, u(0, 0, np.pi / 4))
        self.calculator.pass_multi_gate(qubit_2, qubit_4, paulix())
        self.calculator.pass_single_gate(qubit_4, u(0, 0, (-1 * np.pi / 4)))
        self.calculator.pass_multi_gate(qubit_1, qubit_4, paulix())
        self.calculator.pass_single_gate(qubit_4, u(0, 0, np.pi / 4))
        self.calculator.pass_multi_gate(qubit_2, qubit_4, paulix())
        self.calculator.pass_single_gate(qubit_4, u(0, 0, (-1 * np.pi / 4)))
        self.calculator.pass_single_gate(qubit_4, u(np.pi / 2, 0, np.pi))
        self.calculator.pass_single_gate(qubit_4, u(0, 0, np.pi / 4))
        self.calculator.pass_multi_gate(qubit_3, qubit_4, paulix())
        self.calculator.pass_single_gate(qubit_4, u(0, 0, (-1 * np.pi / 4)))
        self.calculator.pass_single_gate(qubit_4, u(np.pi / 2, 0, np.pi))
        self.circuit_drawing.add_block("RC3X", [qubit_1, qubit_2, qubit_3, qubit_4])

    def swap(self, qubit_one: int, qubit_two: int) -> None:
        self.calculator.pass_multi_gate(qubit_one, qubit_two, paulix())
        self.calculator.pass_multi_gate(qubit_two, qubit_one, paulix())
        self.calculator.pass_multi_gate(qubit_one, qubit_two, paulix())
        self.circuit_drawing.add_swap(qubit_one, qubit_two)

    def rxx(self, qubit_one: int, qubit_two: int, theta: float = np.pi / 2) -> None:
        self.calculator.pass_single_gate(
            qubit_one, u(phi=theta, lmbda=0, theta=np.pi / 2)
        )
        self.calculator.pass_single_gate(qubit_two, hadamard())
        self.calculator.pass_multi_gate(qubit_one, qubit_two, paulix())
        self.calculator.pass_single_gate(qubit_two, u(-1 * theta, 0, 0))
        self.calculator.pass_multi_gate(qubit_one, qubit_two, paulix())
        self.calculator.pass_single_gate(
            qubit_one, u(np.pi / 2, -1 * np.pi, np.pi - theta)
        )
        self.calculator.pass_single_gate(qubit_two, hadamard())
        self.circuit_drawing.add_block("RXX", [qubit_one, qubit_two])

    def rzz(self, qubit_one: int, qubit_two: int, lmbda: float = np.pi / 2) -> None:
        self.calculator.pass_multi_gate(qubit_one, qubit_two, paulix())
        self.calculator.pass_single_gate(qubit_two, u(0, lmbda, 0))
        self.calculator.pass_multi_gate(qubit_one, qubit_two, paulix())
        self.circuit_drawing.add_block("RZZ", [qubit_one, qubit_two])
