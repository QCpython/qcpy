"""
quantumcircuit.py
"""
from ..qubit import qubit
from ..quantumgate import *
from .tools import amplitude, phaseangle, probabilities, measure
import numpy as np

"""
Purpose:
    To apply various quantum gates to a quantum wire given any amount of qubits. With this, to then return the state at any given moment
    alongside calculations to be examined upon.
Methods:
    __init__:
        Constructor that initilizes the quantum state in a vector given the number of qubits, endian positioning, and prepping of the qubits.
    __operator_matrix__:
        Return a matrix from the tensor product calculation algorithm from any inplaced quantum gate.
    __controlled_phase_handler__:
        Calls a control_qubit and target_qubit qubits represented as integers and will then correctly create a system of mathematic implementations of
        any given controlled quantum gate.
    circuit:
        Returns the dictionary representation of the circuit and the values within it.
    amplitude:
        Return a vector of all possible amplitudes for the given state.
    phaseAngle:
        Calculates an array of possible phase angles based off the state. Converts each value using np.angle() function then degree to radian.
    state:
        Return a numpy array of the current quantum circuit.
    probabilities:
        Return a matrix with all the probabilities for each state.
    measure:
        Collapes the quantum circuit into classical bits.
    reverse:
        Reverses the quantum state.
    toffoli:
        A 3-qubit quantum gate that takes in two control_qubit qubits and one target_qubit qubit.
    rccx:
        A 3-qubit quantum gate that takes in two control_qubit qubits and one target_qubit qubit.
    rc3x:
        A 4-qubit quantum gate that is a simplified Toffoli gate and can be used in placed where the Toffoli gate is uncomputed again.
    cnot:
        A 2-qubit quantum gate that takes in control_qubit and target_qubit qubits, and will entangle the qubits if the control_qubit qubit is greater than 0.
    cr:
        A 2-qubit quantum gate that takes in control_qubit and target_qubit qubits to perform calculations upon the state.
    cz:
        A 2-qubit quantum gate that takes in control_qubit and target_qubit qubits to perform calculations upon the state.
    swap:
        A 2-qubit quantum gate that takes in two qubits to swap the qubits values they represent.
    rxx:
        A 2-qubit quantum gate that takes in two qubits and a representation of theta to initialize in the quantum state.
    rzz:
        A 2-qubit quantum gate that takes in two qubits and a representation of theta to initialize in the quantum state.
    customControlPhase:
        Used to insert single qubit based quantum gates to have a control_qubit qubit apart of it and committing to the quantum state.
    identity:
        Used to confirm value that a qubit is representing and does nothing to manipulate the value of such qubit.
    x:
        Used to invert the value of what a qubit is representing.
    hadamard:
        Used to put a given qubit into superposition.
    y:
        Changes the state of a qubit by pi around the y-axis of a Bloch Sphere.
    z:
        Changes the state of a qubit by pi around the z-axis of a Bloch Sphere.
    phase:
        Commits to a rotation around the z-axis based off of the inputted theta value.
    s:
        Is a Phase gate where the inputted theta value is given as a constant of theta = pi / 2.
    sdg:
        Is a Phase gate and inverse of the S gate where the inputted theta value is given as a constant of theta = -pi / 2.
    t:
        T gate is a special use case gate that in implemented from the P Gate.
    tdg:
        TDG gate is a special use case gate that in implemented from the P Gate and is the inverse of the T gate.
    rz:
        RZ gate commits a rotation around the z-axis for a qubit.
    ry:
        RY gate commits a rotation around the y-axis for a qubit.
    rx:
        RX gate commits a rotation around the x-axis for a qubit.
    sx:
        SX gate is the square root of the Inverse gate (X, PauliX Gate).
    sxdg:
        SXDG gate is the negative square root of the Inverse gate (X, PauliX Gate) and inverse of the SX gate.
    u:
        U gate is given three inputs (theta, phi, and lambda) that allow the inputs to manipulate the base matrix to allow for the position of the enacted qubit
        around the bloch sphere representation.
    custom:
        Will take in a custom single qubit quantum gate and implement it on a qubit.
--------

"""


class quantumcircuit:
    def __init__(
            self,
            qubits: int,
            little_endian: bool = False,
            prep: chr = 'z'):
        """
        Constructor that initilizes the quantum state in a vector given the
        number of qubits, endian positioning, and prepping of the qubits.
        Args:
            qubits:
                The number of qubits that will be within the circuit.
            little_endian:
                a boolean variable to determine the placement of values, as
                well as determining the inverse of tensor product.
            prep:

        ------
        Variables:
            _little_endian :
                the number of qubits on the circuit
            _circuit_size :
                all the states of the qubits on the circuit
            _probabilities :
                an array of all the probabilities of the qubits being measured
            _percents :
                the array of probabilities turned into an array of values adding
                to 100
            _state :
                the state values for the qubit being taken into consideration
        """
        if (qubits < 1):
            exit(
                f"Error: QuantumCircuit().__init__ -- Quantum Circuit size must \
                be 1 or more qubits. Current number of qubits is: {qubits}")

        self._little_endian = little_endian

        self._circuit_size = qubits

        self._circuit = []
        self.state = qubit(prep)

        for _ in range(qubits - 1):

            self.state = np.kron(self.state, qubit(prep))

    def __operator_matrix__(
            self,
            gate_matrix: np.array,
            qubit: int,
            double: bool = False):
        """
        Return a matrix from the tensor product calculation algorithm from any
        inplaced quantum gate.
        Params:
            gate_matrix: np.array
            qubit: integer
            double: boolean
        Returns:
            operator_matrix (numpy array):
                Matrix after final calculation from the tensor product algorithm.
        """

        i_matrix = identity()
        gate_queue = [i_matrix for _ in range(self._circuit_size)]
        gate_queue[qubit] = gate_matrix

        if double:
            gate_queue.pop(qubit + 1)

        if (self._little_endian):

            gate_queue = gate_queue[::-1]

        operator_matrix = gate_queue[0]

        for gate in gate_queue[1:]:

            operator_matrix = np.kron(operator_matrix, gate)

        return operator_matrix

    def __controlled_phase_handler__(
            self,
            matrix_to_calculate: np.array,
            control_qubit: int,
            target_qubit: int):
        """
        Calls a control_qubit and target_qubit represented as integers and will
        then correctly create a system of mathematic implementations of any
        given controlled quantum gate.
        Params:
            matrix_to_calculate: np.array
            control_qubit: integer
            target_qubit: integer
        Returns:
            None.
        """

        if matrix_to_calculate.shape != (2, 2):
            matrix_to_calculate = matrix_to_calculate[-2:, -2:]

        bra_ket_zero = np.array([[1 + 0j, 0 + 0j],
                                [0 + 0j, 0 + 0j]], 'F')

        bra_ket_one = np.array([[0 + 0j, 0 + 0j],
                                [0 + 0j, 1 + 0j]], 'F')

        bra_ket_zero_kron = [identity()] * self._circuit_size

        bra_ket_one_kron = [identity()] * self._circuit_size

        bra_ket_zero_kron[control_qubit] = bra_ket_zero
        bra_ket_one_kron[control_qubit] = bra_ket_one
        bra_ket_one_kron[target_qubit] = matrix_to_calculate

        if self._little_endian:

            bra_ket_zero_kron = bra_ket_zero_kron[::-1]
            bra_ket_one_kron = bra_ket_one_kron[::-1]

        to_add_zero = bra_ket_zero_kron[0]

        to_add_one = bra_ket_one_kron[0]

        for i in range(1, len(bra_ket_zero_kron)):

            to_add_zero = np.kron(to_add_zero, bra_ket_zero_kron[i])

            to_add_one = np.kron(to_add_one, bra_ket_one_kron[i])

        to_add_zero += to_add_one

        self.state = np.dot(
            to_add_zero,
            self.state)
        return

    def circuit(self):
        """
        Returns the dictionary representation of the circuit and the values within it.
        Params:
            None.
        Returns:
            np.array self._circuit
        """
        return self._circuit

    def amplitude(self, show_bit=-1, round: int = 3, radian: bool = False):
        """
        Return a vector of all possible amplitudes for the given state.
        Params:
            show_bit: string or int
            round: int
            radian: bool
        Returns:
            np.around(statevector) (numpy array):
                Matrix after final calculation from the sqrt(x^2 + y^2) algorithm for finding the amplitude.
        """
        return amplitude(
            self.state,
            self._circuit_size,
            show_bit,
            round,
            radian)

    def phaseangle(self, show_bit=-1, round: int = 3, radian: bool = True):
        """
        Calculates an array of possible phase angles based off the state. Converts each value using np.angle() function then degree to radian.
        Params:
            show_bit: string or int
            round: int
            radian: bool
        Returns:
            np.around(phaseAngles) (numpy array):
                Matrix after final calculation from the phase angle algorithm.
        """
        return phaseangle(
            self.state,
            self._circuit_size,
            show_bit,
            round,
            radian)

    def circuitqueue(self):
        return self._circuit

    def circuitsize(self):
        return self._circuit_size

    def probabilities(
            self,
            show_percent: bool = False,
            show_bit: int = -1,
            round: int = 3):
        """
        Return a matrix with all the probabilities for each state
        Params:
            show_percent: bool
            show_bit: string or int
            round: int
        Returns:
            prob_matrix (numpy array):
                matrix with all the weighted probabilities of being measured
        """
        return probabilities(
            self.state,
            self._circuit_size,
            show_percent,
            show_bit,
            round)

    def measure(self):
        """
        Collapes the quantum circuit into classical bits
        Params:
            None
        Returns:
            final_state (str):
                the winning state displayed in classical bits notation
        """

        return measure(self.state, self._circuit_size, self.probabilities())

    def reverse(self):
        """
        Reverses the quantum state.
        Params:
            None.
        Returns:
            None.
        """

        self.state = self.state[::-1]

    def flatten(self, round: int = 3):
        """
        Return a numpy array of the current quantum circuit.
        Params:
            round: int
        Returns:
            np.around(self._state) (numpy array):
                vector of the given state rounded based off of the parameter
        """
        if (round < 0):
            exit(
                f"Error: QuantumCircuit().state -- round placement must be a value greater than 0.")
        return np.around(self.state, decimals=round).flatten()
    """
    Multiple qubit quantum gates
    """

    def toffoli(self, control_1: int, control_2: int, target_qubit: int):
        """
        A 3-qubit quantum gate that takes in two control_qubit qubits and one target_qubit qubit.
        Params:
            control_1: int
            control_2: int
            target_qubit: int
        Returns:
            None.
        """

        if (self._circuit_size < 3):
            exit(
                f"Error: QuantumCircuit().toffoli -- Quantum Circuit size must be 3 or more qubits. Current number of qubits is: {self._circuit_size}")

        self.customcontrolled(control_2, target_qubit, sx())
        self.cnot(control_1, control_2)
        self.customcontrolled(control_2, target_qubit, sxdg())
        self.cnot(control_1, control_2)
        self.customcontrolled(control_1, target_qubit, sx())

        self._circuit.append(('toffoli', control_1, control_2, target_qubit))

    def rccx(self, control_1: int, control_2: int, target_qubit: int):
        """
        A 3-qubit quantum gate that takes in two control_qubit qubits and one target_qubit qubit.
        Params:
            control_1: int
            control_2: int
            target_qubit: int
        Returns:
            None.
        """

        if (self._circuit_size < 3):
            exit(
                f"Error: QuantumCircuit().rccx -- Quantum Circuit size must be 3 or more qubits. Current number of qubits is: {self._circuit_size}")

        self.u(target_qubit, np.pi / 2, 0, np.pi)
        self.u(target_qubit, 0, 0, np.pi / 4)
        self.cnot(control_2, target_qubit)
        self.u(target_qubit, 0, 0, (-1 * np.pi) / 4)
        self.cnot(control_1, target_qubit)
        self.u(target_qubit, 0, 0, np.pi / 4)
        self.cnot(control_2, target_qubit)
        self.u(target_qubit, 0, 0, (-1 * np.pi) / 4)
        self.u(target_qubit, np.pi / 2, 0, np.pi)

        self._circuit.append(('rccx', control_1, control_2, target_qubit))

    def rc3x(self, qubit_1: int, qubit_2: int, qubit_3: int, qubit_4: int):
        """
        A 4-qubit quantum gate that is a simplified Toffoli gate and can be used in placed where the Toffoli gate is uncomputed again.
        Params:
            a: int
            b: int
            c: int
            d: int
        Returns:
            None.
        """

        if (self._circuit_size < 4):
            exit(
                f"Error: QuantumCircuit().rc3x -- Quantum Circuit size must be 4 or more qubits. Current number of qubits is: {self._circuit_size}")

        self.u(qubit_4, np.pi / 2, 0, np.pi)
        self.u(qubit_4, 0, 0, np.pi / 4)
        self.cnot(qubit_3, qubit_4)
        self.u(qubit_4, 0, 0, (-1 * np.pi) / 4)
        self.u(qubit_4, np.pi / 2, 0, np.pi)
        self.cnot(qubit_1, qubit_4)
        self.u(qubit_4, 0, 0, np.pi / 4)
        self.cnot(qubit_2, qubit_4)
        self.u(qubit_4, 0, 0, (-1 * np.pi / 4))
        self.cnot(qubit_1, qubit_4)
        self.u(qubit_4, 0, 0, np.pi / 4)
        self.cnot(qubit_2, qubit_4)
        self.u(qubit_4, 0, 0, (-1 * np.pi) / 4)
        self.u(qubit_4, np.pi / 2, 0, np.pi)
        self.u(qubit_4, 0, 0, np.pi / 4)
        self.cnot(qubit_3, qubit_4)
        self.u(qubit_4, 0, 0, (-1 * np.pi / 4))
        self.u(qubit_4, np.pi / 2, 0, np.pi)

        self._circuit.append(('rc3x', qubit_1, qubit_2, qubit_3, qubit_4))

    def cnot(self, control_qubit: int, target_qubit: int):
        """
        A 2-qubit quantum gate that takes in control_qubit and target_qubit qubits, and will entangle the qubits if the control_qubit qubit is greater than 0.
        Params:
            control_qubit: int
            target_qubit: int
        Returns:
            None.
        """

        if (self._circuit_size < 2):
            exit(
                f"Error: QuantumCircuit().cnot -- Quantum Circuit size must be 2 or more qubits. Current number of qubits is: {self._circuit_size}")

        self.__controlled_phase_handler__(
            paulix(), control_qubit, target_qubit)

        self._circuit.append(('cnot', control_qubit, target_qubit))

    def cr(self, control_qubit: int, target_qubit: int):
        """
        A 2-qubit quantum gate that takes in control_qubit and target_qubit qubits to perform calculations upon the state.
        Params:
            control_qubit: int
            target_qubit: int
        Returns:
            None.
        """
        if (self._circuit_size < 2):
            exit(
                f"Error: QuantumCircuit().cr -- Quantum Circuit size must be 2 or more qubits. Current number of qubits is: {self._circuit_size}")
        self.__controlled_phase_handler__(
            cr(), control_qubit, target_qubit)

    def cz(self, control_qubit: int, target_qubit: int):
        """
        A 2-qubit quantum gate that takes in control_qubit and target_qubit qubits to perform calculations upon the state.
        Params:
            control_qubit: int
            target_qubit: int
        Returns:
            None.
        """
        if (self._circuit_size < 2):
            exit(
                f"Error: QuantumCircuit().cz -- Quantum Circuit size must be 2 or more qubits. Current number of qubits is: {self._circuit_size}")
        self.__controlled_phase_handler__(
            cz(), control_qubit, target_qubit)

    def swap(self, qubit_1: int, qubit_2: int):
        """
        A 2-qubit quantum gate that takes in two qubits to swap the qubits values they represent.
        Params:
            qubit_1: int
            qubit_2: int
        Returns:
            None.
        """

        if (self._circuit_size < 2):
            exit(
                f"Error: QuantumCircuit().swap -- Quantum Circuit size must be 2 or more qubits. Current number of qubits is: {self._circuit_size}")
        self.cnot(qubit_1, qubit_2)
        self.cnot(qubit_2, qubit_1)
        self.cnot(qubit_1, qubit_2)
        self._circuit.append(('swap', qubit_1, qubit_2))

    def rxx(self, qubit_1: int, qubit_2: int, theta: float = np.pi / 2):
        """
        A 2-qubit quantum gate that takes in two qubits and a representation of theta to initialize in the quantum state.
        Params:
            qubit_1: int
            qubit_2: int
            theta: float
        Returns:
            None.
        """
        # If circuit is less than 2, means RXX gate cannot be allowed.
        if (self._circuit_size < 2):
            exit(
                f"Error: QuantumCircuit().rxx -- Quantum Circuit size must be 2 or more qubits. Current number of qubits is: {self._circuit_size}")
        self.u(qubit_1, phi=theta, lmbda=0, theta=np.pi / 2)
        self.h(qubit_2)
        self.cnot(qubit_1, qubit_2)
        self.u(qubit_2, lmbda=-1 * theta, theta=0, phi=0)
        self.cnot(qubit_1, qubit_2)
        self.u(qubit_1, theta=np.pi / 2, phi=-1 *
               np.pi, lmbda=np.pi - theta)
        self.h(qubit_2)

        # append gate to self._circuit
        self._circuit.append(('rxx', qubit_1, qubit_2))

    def rzz(self, qubit_1: int, qubit_2: int, theta: float = np.pi / 2):
        """
        A 2-qubit quantum gate that takes in two qubits and a representation of theta to initialize in the quantum state.
        Params:
            qubit_1: int
            qubit_2: int
            theta: float
        Returns:
            None.
        """
        # If circuit is less than 2, means RZZ gate cannot be allowed.
        if (self._circuit_size < 2):
            exit(
                f"Error: QuantumCircuit().rzz -- Quantum Circuit size must be 2 or more qubits. Current number of qubits is: {self._circuit_size}")
        if (qubit_1 > qubit_2):
            self.h(qubit_1)
            self.h(qubit_2)

        self.cnot(qubit_1, qubit_2)
        self.u(qubit_2, theta=0, phi=0, lmbda=np.pi / 2)
        self.cnot(qubit_1, qubit_2)
        if (qubit_1 > qubit_2):
            self.h(qubit_1)
            self.h(qubit_2)

    def customcontrolled(
            self,
            control_qubit: int,
            target_qubit: int,
            custom_matrix: np.array):
        """
        Used to insert single qubit based quantum gates to have a control_qubit qubit apart of it and committing to the quantum state.
        Params:
            control_qubit: int
            target_qubit: int
            custom_matrix: np.array
        Returns:
            None.
        """

        if (custom_matrix.shape != (2, 2)):
            exit(f"Error: QuantumCircuit().customControlPhase -- can only include a single qubit based quantum gate (2,2) matrix for state manipulation.")

        self.__controlled_phase_handler__(
            custom_matrix, control_qubit, target_qubit)
        self._circuit.append(('C', control_qubit, target_qubit))

    """
    Single Qubit Gates
    """

    def i(self, qubit: int):
        """
        Used to confirm value that a qubit is representing and does nothing to manipulate the value of such qubit.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().identity -- Must select a qubit to enact on quantum gate.")
        self.state = np.dot(
            self.__operator_matrix__(
                identity(),
                qubit),
            self.state)

    def x(self, qubit: int):
        """
        Used to invert the value of what a qubit is representing.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().x -- Must select a qubit to enact on quantum gate.")
        # get the not matrix
        self.state = np.dot(
            self.__operator_matrix__(
                paulix(), qubit), self.state)

    def h(self, qubit: int):
        """
        Used to put a given qubit into superposition.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().hadamard -- Must select a qubit to enact on quantum gate.")
        # get the hadamard matrix
        self.state = np.dot(
            self.__operator_matrix__(
                hadamard(), qubit), self.state)

    def y(self, qubit: int):
        """
        Changes the state of a qubit by pi around the y-axis of a Bloch Sphere.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().y -- Must select a qubit to enact on quantum gate.")
        # get the Y matrix
        self.state = np.dot(
            self.__operator_matrix__(
                pauliy(), qubit), self.state)

    def z(self, qubit: int):
        """
        Changes the state of a qubit by pi around the z-axis of a Bloch Sphere.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().z -- Must select a qubit to enact on quantum gate.")
        # get the Z matrix
        self.state = np.dot(
            self.__operator_matrix__(
                pauliz(), qubit), self.state)

    def phase(self, qubit: int, theta: float = np.pi / 2):
        """
        Commits to a rotation around the z-axis based off of the inputted theta value.
        Params:
            qubit: int
            theta: float
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().phase -- Must select a qubit to enact on quantum gate.")
        # get the Phase matrix
        self.state = np.dot(
            self.__operator_matrix__(
                phase(theta), qubit), self.state)

    def s(self, qubit: int):
        """
        Is a Phase gate where the inputted theta value is given as a constant of theta = pi / 2.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().s -- Must select a qubit to enact on quantum gate.")
        # get the Phase matrix
        self.state = np.dot(
            self.__operator_matrix__(
                s(), qubit), self.state)

    def sdg(self, qubit: int):
        """
        Is a Phase gate and inverse of the S gate where the inputted theta value is given as a constant of theta = -pi / 2.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().sdg -- Must select a qubit to enact on quantum gate.")
        # get the Sdg matrix
        self.state = np.dot(
            self.__operator_matrix__(
                sdg(), qubit), self.state)

    def t(self, qubit: int):
        """
        T gate is a special use case gate that in implemented from the P Gate.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().t -- Must select a qubit to enact on quantum gate.")
        # get the T matrix
        self.state = np.dot(
            self.__operator_matrix__(
                t(), qubit), self.state)

    def tdg(self, qubit: int):
        """
        TDG gate is a special use case gate that in implemented from the P Gate and is the inverse of the T gate.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().tdg -- Must select a qubit to enact on quantum gate.")
        # get the Tdg matrix
        self.state = np.dot(
            self.__operator_matrix__(
                tdg(), qubit), self.state)

    def rz(self, qubit: int, theta: float = np.pi / 2):
        """
        RZ gate commits a rotation around the z-axis for a qubit.
        Params:
            qubit: int
            theta: float
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().rz -- Must select a qubit to enact on quantum gate.")
        # get the Rz matrix
        self.state = np.dot(
            self.__operator_matrix__(
                rz(theta), qubit), self.state)

    def ry(self, qubit: int, theta: float = np.pi / 2):
        """
        RY gate commits a rotation around the y-axis for a qubit.
        Params:
            qubit: int
            theta: float
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().ry -- Must select a qubit to enact on quantum gate.")
        # get the Ry matrix
        self.state = np.dot(
            self.__operator_matrix__(
                ry(theta), qubit), self.state)

    def rx(self, qubit: int, theta: float = np.pi / 2):
        """
        RX gate commits a rotation around the x-axis for a qubit.
        Params:
            qubit: int
            theta: float
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().rx -- Must select a qubit to enact on quantum gate.")
        # get the Rx matrix
        self.state = np.dot(
            self.__operator_matrix__(
                rx(theta), qubit), self.state)

    def sx(self, qubit: int):
        """
        SX gate is the square root of the Inverse gate (X, PauliX Gate).
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().sx -- Must select a qubit to enact on quantum gate.")
        # get the Sx matrix
        self.state = np.dot(
            self.__operator_matrix__(
                sx(), qubit), self.state)

    def sxdg(self, qubit: int):
        """
        SXDG gate is the negative square root of the Inverse gate (X, PauliX Gate) and inverse of the SX gate.
        Params:
            qubit: int
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().sxdg -- Must select a qubit to enact on quantum gate.")
        # get the Sxdg matrix
        self.state = np.dot(
            self.__operator_matrix__(
                sxdg(), qubit), self.state)

    def u(
        self,
        qubit: int,
        theta: float = np.pi / 2,
        phi: float = np.pi / 2,
            lmbda: float = np.pi / 2):
        """
        U gate is given three inputs (theta, phi, and lambda) that allow the inputs to manipulate the base matrix to allow for the position of the enacted qubit
        around the bloch sphere representation.
        Params:
            qubit: int
            theta: float
            phi: float
            lmbda: float
        Returns:
            None.
        """
        if qubit is None:
            exit(
                f"Error: QuantumCircuit().u -- Must select a qubit to enact on quantum gate.")
        # get the U matrix
        self.state = np.dot(
            self.__operator_matrix__(
                u(theta, phi, lmbda), qubit), self.state)

    def custom(self, qubit: int, custom_matrix: np.array):
        """
        Will take in a custom single qubit quantum gate and implement it on a qubit.
        Params:
            qubit: int
            custom_matrix: np.array
        Returns:
            None.
        """
        # if gate is not a single qubit, will exit.
        if (custom_matrix.shape != (2, 2)):
            exit(f"Error: QuantumCircuit().insertGate -- can only include a single qubit based quantum gate (2,2) matrix for state manipulation.")
        # calls gate and will operate on state as per usual
        self.state = np.dot(
            self.__operator_matrix__(
                custom_matrix,
                qubit),
            self.state)
