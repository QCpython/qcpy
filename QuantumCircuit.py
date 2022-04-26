"""
QuantumCircuit.py
"""
from .Qubit import Qubit
from .QuantumGate import *
import numpy as np

"""
Purpose: To Interpret the Gates and present the calculated information through the probabilities, amplitude, etc.

Methods
--------

__operator_matrix__(gate_matrix: np.array, qubit: int, double: bool = False) :
    Returns the tensor product of the desired gates, see method itself for more information.
amplitude():
    Returns an array of values to signify the amplitude of each and every value possible from the state.
phaseAngle():
    Returns the radian value for each and every possible value within the state it is being applied to.
state():
    Returns the initial state values within a vector state.
probabilities():
    Returns all probabilities from the possible values found within the state.
measure():
    Returns the measurement of the state and will result in a random collapsing.
cnot():
    Calls the CNOT gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
x():
    Calls the PauliX gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
y():
    Calls the PauliY gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
z():
    Calls the PauliZ gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
swap():
    Calls the SWAP gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
toffoli():
    Calls the TOFFOLI gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
phase():
    Calls the Phase gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
hadamard():
    Calls the Hadamard gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
s():
    Calls the S gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
sdg():
    Calls the SDG gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
t():
    Calls the T gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
tdg():
    Calls the TDG gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
rz():
    Calls the RZ gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
rx():
    Calls the RX gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
ry():
    Calls the RY gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
sx():
    Calls the SX gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
sxdg():
    Calls the SXDG gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
u():
    Calls the U gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
rxx():
    Calls the RXX gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
rzz():
    Calls the RZZ gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.

"""

class QuantumCircuit:
    def __init__(self, qubits: int, little_endian: bool = False):
        """
        Args:
            qubits: 
                The number of qubits that will be within the circuit.
            little_endian:
                a boolean variable to determine the placement of values, as well as determining the inverse of tensor product.
        ------
        Variables:
            _little_endian : 
                the number of qubits on the circuit
            _circuit_size :
                all the states of the qubits on the circuit
            _probabilities :
                an array of all the probabilities of the qubits being measured
            _percents :
                the array of probabilities turned into an array of values adding to 100
            _state :
                the state values for the qubit being taken into consideration
        """
        # Determines if tensor calculation of __operator_matrix__ will be reversed or not
        self._little_endian = little_endian
        # Gets the number of qubits in play to store for later use.
        self._circuit_size = qubits
        # Makes tensored vector state of all qubits, and stores it within _state to get a vector of [[1], [0], [0],....2^n]
        self._state = Qubit(0).state
        for i in range(qubits-1):
            self._state = np.kron(self._state, Qubit(0).state)
        # end of constructor
    def __operator_matrix__(self, gate_matrix: np.array, qubit: int, double: bool = False):
        """
        Return a matrix from the tensor product calculation algorithm from any inplaced quantum gate.
        Params:
            gate_matrix: np.array
            qubit: integer
            double: boolean
        Returns:
            operator_matrix (numpy array): 
                Matrix after final calculation from the tensor product algorithm.
        """
        i_matrix = Identity().matrix
        # gate queue for the computation
        gate_queue = [i_matrix for i in range(self._circuit_size)]
        # replaces the placement of the identity gate at the qubit index with the gate to get a correct calculation of final product
        gate_queue[qubit] = gate_matrix
        # if double is true, then CNOT, toffli, or any gate more than one qubit is being asked to be implemented.
        if double:
            gate_queue.pop(qubit+1)
        # if little_endian variable is true to follow IBM and Qiskit notation. Inverses queue of operation
        if (self._little_endian):
            gate_queue = gate_queue[::-1]
        # stores final value to be stored into operator_matrix value
        operator_matrix = gate_queue[0]
        # uses np.kron() function to tensor product the queue
        for gate in gate_queue[1:]:
            operator_matrix = np.kron(operator_matrix, gate)
        return operator_matrix
    def amplitude(self, round: int = 3):
        """
        Return a vector of all possible amplitudes for the given state.
        Params:
            round: int 
        Returns:
            np.around(statevector) (numpy array): 
                Matrix after final calculation from the sqrt(x^2 + y^2) algorithm for finding the amplitude.
        """
        # initial array for return 
        statevector = []
        # for loop will go through this statement 2^n times for _state length
        for i in range(len(self._state)):
            #calculates sqrt(x^2 + y^2 for amplitude), x = real value, y = imaginary value
            statevector.append(np.sqrt(np.power(self._state[i].real, 2) + np.power(self._state[i].imag, 2)))
        # rounds value based off of parameter
        return np.around(statevector, decimals = round)
    def phaseAngle(self, round: int = 2):
        """
        Calculates an array of possible phase angles based off the state. Converts each value using np.angle() function then degree to radian.
        Params:
            round: int 
        Returns:
            np.around(phaseAngles) (numpy array): 
                Matrix after final calculation from the  phase angle algorithm.
        """
        # initial array for return
        phaseAngles = []
        # for loop will calculate based off of 2^n times.
        for i in range(len(self._state)):
            # calls degrees of the state in its complex format.
            angle = np.angle(self._state[i], deg = True)
            # determines if it is a negative value, in which case it will need to add 360 to get a true angle value.
            if (angle[0] < 0):
                angle[0] += 360
            # appends the degrees value to radians from the previous function call.
            deg2rad = np.deg2rad(angle)
            if (deg2rad >= (np.pi * 2)):
                deg2rad = deg2rad % np.pi
            phaseAngles.append(deg2rad)

        return np.around(phaseAngles, decimals = round)
    def state(self, round: int = 3):
        """
        Return a vector of all possible phase angles for the given state.
        Params:
            round: int 
        Returns:
            np.around(self._state) (numpy array): 
                vector of the given state rounded based off of the parameter
        """
        return np.around(self._state, decimals = round)
    def probabilities(self, round: int = 3):
        """
        Return a matrix with all the probabilities for each state
        Params:
            None
        Returns:
            prob_matrix (numpy array): 
                matrix with all the weighted probabilities of being measured
        """
        # get the probabilties for the "winner" of the measurement at any single point on the circuit
        prob_matrix = self._state
        # collapse the circuit into 1D
        prob_matrix = prob_matrix.flatten()
        # square the values to get the probabilities of each qubit state
        prob_matrix = np.square(prob_matrix)
        # turn all the complex numbers into real values
        prob_matrix = np.abs(prob_matrix)
        prob_matrix = np.around(prob_matrix, decimals=self._circuit_size)
        return prob_matrix
    def measure(self):
        """
        Collapes the quantum circuit into classical bits
        Params:
            None
        Returns:
            final_state (str): 
                the winning state displayed in classical bits notation
        """
        # randomly selects the measured state using self.probabilities()
        prob_matrix = self.probabilities()
        num_bits = self._circuit_size # number of bits
        state_list = [format(i, 'b').zfill(num_bits) for i in range(2**num_bits)] # creates a list of bits in strings
        state_list = list(map(int, state_list)) # turns state_list from list of strings to list of ints
        # numpy.random.choice takes in the list we will select from, size of the returning list,
        #   and p = weights of each element 
        final_state = np.random.choice(state_list, 1, p = prob_matrix)
        final_state = str(final_state[0]) # take out the bits from the returned list and convert to a string
        final_state = final_state.zfill(num_bits) # pad with zeroes if needed
        return final_state  # return the final state
    def toffoli(self, control_1: int, control_2: int, target: int):
        self.hadamard(target)
        self.cnot(control_2, target)
        self.tdg(target)
        self.cnot(control_1, target)
        self.t(target)
        self.cnot(control_2, target)
        self.tdg(target)
        self.cnot(control_1, target)
        self.t(control_2)
        self.t(target)
        self.cnot(control_1, control_2)
        self.hadamard(target)
        self.t(control_1)
        self.tdg(control_2)
        self.cnot(control_1, control_2)
    def cnot(self, control: int, target: int):
        # inverse bool
        inverse = False
        # checking to see if target is less than control indices:
        if(target < control):
            cnot_matrix = CNot(inverse = True).matrix
            inverse = True
        else:
            cnot_matrix = CNot().matrix
        # create temp target variable
        temp_target = target
        if(target-control == 1 or target-control == -1):
                if inverse:
                    self._state = np.dot(self.__operator_matrix__(cnot_matrix, target, double=True), self._state)
                else:
                    self._state = np.dot(self.__operator_matrix__(cnot_matrix, control, double=True), self._state)
                return
        # while the difference between the temp target and control is not -1 or 1
        while(temp_target - control != 1 and temp_target - control != -1):
            # if the distance between target and control is already 1
            if inverse:
                # swap the temp target closer to the target
                self.swap(temp_target, temp_target+1)
                # update temp target position
                temp_target += 1
            else:
                # swap the temp target closer to the target
                self.swap(temp_target-1, temp_target)
                # update temp target position
                temp_target -= 1
        # perform cnot operation
        if inverse:
            self._state = np.dot(self.__operator_matrix__(cnot_matrix, temp_target, double=True), self._state)
        else:
            self._state = np.dot(self.__operator_matrix__(cnot_matrix, control, double=True), self._state)
        # while the temp target does not equal the original target
        while(temp_target != target):
            if inverse:
                # swap the temp target with the position closer to original target
                self.swap(temp_target-1, temp_target)
                # update temp target position
                temp_target -=1
            else:
                # swap the temp target with the position closer to original target
                self.swap(temp_target, temp_target+1)
                # update temp target position
                temp_target +=1
    def x(self, qubit: int):
        # get the not matrix
        x_matrix = PauliX().matrix
        self._state = np.dot(self.__operator_matrix__(x_matrix, qubit), self._state)
    def hadamard(self, qubit: int):
        # get the hadamard matrix
        h_matrix = Hadamard().matrix
        self._state = np.dot(self.__operator_matrix__(h_matrix, qubit), self._state)
    def y(self, qubit: int):
        # get the Y matrix
        y_matrix = PauliY().matrix
        self._state = np.dot(self.__operator_matrix__(y_matrix, qubit), self._state)
    def z(self, qubit: int):
        # get the Z matrix
        z_matrix = PauliZ().matrix
        self._state = np.dot(self.__operator_matrix__(z_matrix, qubit), self._state)
    def phase(self, qubit: int, theta: float = np.pi / 2):
        # get the Phase matrix
        phase_matrix = Phase(theta).matrix
        self._state = np.dot(self.__operator_matrix__(phase_matrix, qubit), self._state)
    def s(self, qubit: int):
        # get the Phase matrix
        phase_matrix = S().matrix
        self._state = np.dot(self.__operator_matrix__(phase_matrix, qubit), self._state)
    def sdg(self, qubit: int):
        # get the Sdg matrix
        sdg_matrix = Sdg().matrix
        self._state = np.dot(self.__operator_matrix__(sdg_matrix, qubit), self._state)
    def t(self, qubit: int):
        # get the T matrix
        t_matrix = T().matrix
        self._state = np.dot(self.__operator_matrix__(t_matrix, qubit), self._state)
    def tdg(self, qubit: int):
        # get the Tdg matrix
        tdg_matrix = Tdg().matrix
        self._state = np.dot(self.__operator_matrix__(tdg_matrix, qubit), self._state)
    def rz(self, qubit: int, theta: float = np.pi / 2):
        # get the Rz matrix
        rz_matrix = Rz(theta).matrix
        self._state = np.dot(self.__operator_matrix__(rz_matrix, qubit), self._state)
    def ry(self, qubit: int, theta: float = np.pi / 2):
        # get the Ry matrix
        ry_matrix = Ry(theta).matrix
        self._state = np.dot(self.__operator_matrix__(ry_matrix, qubit), self._state)
    def rx(self, qubit: int, theta: float = np.pi / 2):
        # get the Ry matrix
        ry_matrix = Ry(theta).matrix
        self._state = np.dot(self.__operator_matrix__(ry_matrix, qubit), self._state)
    def sx(self, qubit: int):
        # get the Sx matrix
        sx_matrix = Sx().matrix
        self._state = np.dot(self.__operator_matrix__(sx_matrix, qubit), self._state)                                           
    def sxdg(self, qubit: int):
        # get the Sxdg matrix
        sxdg_matrix = Sxdg().matrix
        self._state = np.dot(self.__operator_matrix__(sxdg_matrix, qubit), self._state)
    def u(self, qubit: int, theta: float = np.pi / 2, phi: float = np.pi / 2, lbmda: float = np.pi / 2):
        # get the U matrix
        u_matrix = U(theta, phi, lbmda).matrix
        self._state = np.dot(self.__operator_matrix__(u_matrix, qubit), self._state)
    def swap(self, qubit_1: int, qubit_2: int):
        # the qubits need to be adjacent, so check that first
        if(qubit_1 - qubit_2 != 1 and qubit_1 - qubit_2 != -1):
            return
        # get the swap matrix
        swap_matrix = Swap().matrix
        self._state = np.dot(self.__operator_matrix__(swap_matrix, qubit_1, double=True), self._state)
    def rxx(self, qubit_1: int, qubit_2: int, theta: float = np.pi / 2):
        # the qubits need to be adjacent, so check that first
        if(qubit_1 - qubit_2 != 1 and qubit_1 - qubit_2 != -1):
            return
        rxx_matrix = Rxx().matrix
        self._state = np.dot(self.__operator_matrix__(rxx_matrix, qubit_1, double = True), self._state)
    def rzz(self, qubit_1: int, qubit_2: int, theta: float = np.pi / 2):
        # the qubits need to be adjacent, so check that first
        if(qubit_1 - qubit_2 != 1 and qubit_1 - qubit_2 != -1):
            return
        rzz_matrix = Rzz().matrix
        self._state = np.dot(self.__operator_matrix__(rzz_matrix, qubit_1, double = True), self._state)
        
    def matrixInsert(self, qubit_1: int = -1, qubit_2: int = -1, custom_matrix: np.array = []):
        if((qubit_1 - qubit_2 != 1 and qubit_1 - qubit_2 != -1) or custom_matrix.shape[0] != custom_matrix.shape[1]):
            return
        doub = False
        if (qubit_2 != -1):
            doub = True
        self._state = np.dot(self.__operator_matrix__(custom_matrix, qubit_1, double = doub), self._state)

    