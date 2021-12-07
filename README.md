# QCpy
Quantum Computing Python Library
By Paris Osuch, Brennan Freeze, and Aundre Barras

# QCpy Documentation

## Class QCpy.QuantumCircuit
### Attributes
#### _bit_str
- Type: string
- String of qubits in the quantum circuit
#### _qubit_array
- Type: List
- Array holding Qubit objects representing the state of each wire and its corresponding qubit
### Methods
#### QuantumCircuit.__init__(bit_str)
- Parameters:
bit_str (string): initialized bits for circuit
#### QuantumCircuit.identity(bit)
- Identity-Gate operation on a specified bit.
- Parameters:
bit (int): the n-th bit position of the circuit
- Returns:
None
QuantumCircuit.x(bit)
Pauli-X-Gate operation on a specified bit.
Parameters:
bit (int): the n-th bit position of the circuit
Returns:
None
QuantumCircuit.y(bit)
Pauli-Y-Gate operation on a specified bit.
Parameters:
bit (int): the n-th bit position of the circuit
Returns:
None
QuantumCircuit.z(bit)
Z-Gate operation on a specified bit.
Parameters:
bit (int): the n-th bit position of the circuit
Returns:
None
QuantumCircuit.hadamard(bit)
Hadamard-Gate operation on a specified bit.
Parameters:
bit (int): the n-th bit position of the circuit
Returns:
None
QuantumCircuit.measure()
Collapses quantum circuit in classical bits.
Parameters:
None
Returns:
final_state (string): the final state (bit-string) of the quantum system.
QuantumCircuit.probabilities()
Returns matrix with all probabilities of each state.
Parameters:
None
Returns:
probability_matrix (list): matrix with all weighted probabilities
QuantumCircuit.graph()
Generate matplotlib diagram using probabilities. 
Parameters:
None
Returns:
probabilities.png
Class QCpy.Qubit(state: int)
Attributes
_INIT_STATE
Type: int
The state of the qubit at initialization.
state
Type: 2D Matrix of complex data type
The state of the qubit

Class QCpy.Graph(qubits: probabilities matrix)
Methods
makeGraph()
Parameters:
None
Returns:
PNG file representing the probability of each state

