# QCpy - A Quantum Computer Simulation Library

## About
###### QCpy is an open source project to help those getting into the field of Quantum Computing. This library has emphasized an easy to interpret method calling system as well as mathematically accurate states to be calculated at any given point within the code segments.
###### It is highly recommend to understand linear algebra basics working alongside this library. Please visit a few of the following links if desired: 

* [Microsoft Linear Algebra and Quantum Computing Documentation](https://docs.microsoft.com/en-us/azure/quantum/overview-algebra-for-quantum-computing)
* [IBM Quantum Computing Documentation](https://quantum-computing.ibm.com/composer/docs/iqx/guide/)

## Please install these dependent libraries in their latest versions before using this library:
* Numpy
* Matplotlib

## Qubit.py
###### This is the core element that will set the initial numpy array to:
```
|1|
|0|
```
###### In this basic state, it will be used by all other calculations to transform the quantum state from this classical state

## QuantumGate.py
###### Contains all possible standard gates being used within quantum computing. All Gates are stored in this manner:
```

class * Gate Name Here * :
  self.matrix = np.array(
   * Matrix of gate stored here *
  )

```
#### Identity Gate
```
[1+0j, 0+0j]
[0+0j, 1+0j]
```

#### PauliX Gate (Inverse Gate, X Gate)
```
[0+0j, 1+0j]
[1+0j, 0+0j]
```
#### PauliY Gate (Y Gate)
```
[0+0j, 0-1j]
[0+1j, 0+0j]
```

#### PauliZ Gate
```
[1+0j, 0+0j]
[0+0j, -1+0j]
```

#### Hadamard Gate
```
(1/sqrt(2)) * [1+0j, 1+0j] 
              [1+0J, -1+0j]
```

#### CNOT Gate

```
[1+0j, 0+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 0+0j, 1+0j]
[0+0j, 0+0j, 1+0j, 0+0j]
[0+0j, 1+0j, 0+0j, 0+0j]
```
###### Inversed CNOT Gate
```
[1+0j, 0+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 0+0j, 1+0j]
[0+0j, 0+0j, 0+0j, 1+0j]
[0+0j, 1+0j, 1+0j, 0+0j]
```
#### Swap Gate
```
[1+0j, 0+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 1+0j, 0+0j]
[0+0j, 1+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 0+0j, 1+0j]
```

#### Toffoli Gate
```
[1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]
[0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j]
[0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j]
[0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j]
```

#### Phase Gate
```
[1+0j, 0+0j]
[0+0j, exp(0+1j * theta)]
```

#### S Gate
```
[1+0j, 0+0j]
[0+0j, 0+1j]
```

#### SDG Gate
```
[1+0j, 0+0j]
[0+0j, 0-1j]
```

#### T Gate
```
[1+0j, 0+0j]
[0+0j, e ** ((0+1j * pi) / 4)]
```
#### TDG Gate
```
[1+0j, 0+0j],
[0+0j, e ** ((0-1j * pi) / 4)]
```

#### RZ Gate
```
[exp((0-1j * (theta / 2))), 0+0j]
[0+0j, exp(0+1j * (theta / 2))]
```

#### RX Gate
```
[cos(theta / 2), 0-1j * sin(theta / 2)]
[0-1j * sin(theta / 2), cos(theta / 2)]
```

#### RY Gate
```
[cos(theta / 2), -1 * sin(theta / 2)]
[sin(theta / 2), cos(theta / 2)]
```

#### SX Gate

```
(1 / 2) * [1+1j, 1-1j]
          [1-1j, 1+1j]
```
#### SXDG Gate
```
(1 / 2) * [1-1j, 1+1j]
           [1+1j, 1-1j]
```

#### U Gate

```
[cos(theta / 2), -1 * exp(0+1j * lbmda) * sin(theta / 2)]
[exp(0+1j * phi) * sin(theta / 2), exp(0+1j * (lbmda + phi)) * cos(theta / 2)]])
```


#### RXX Gate
```
[cos(theta / 2), 0+0j, 0+0j, 0-1j * sin(theta / 2)],
[0+0j, cos(theta / 2), 0-1j * sin(theta / 2), 0+0j],
[0+0j, 0-1j * sin(theta / 2), cos(theta / 2), 0+0j],
[ 0-1j * sin(theta / 2), 0+0j, 0+0j, cos(theta / 2)]
```

#### RZZ Gate

```
[exp(0-1j * (theta / 2)), 0+0j, 0+0j, 0+0j],
[0+0j, exp(0+1j * (theta / 2)), 0+0j, 0+0j],
[0+0j, 0+0j, exp(0+1j * (theta / 2)), 0+0j],
[0+0j, 0+0j, 0+0j, exp(0-1j * (theta / 2))]
```
## QuantumCircuit
###### Where all calculations occur. Call the class object and initialize the simulated circuit
###### Please note that the placement of the qubit must be enplaced based off of certain number of qubits needed to complete the gate.

```
circuit = QuantumCircuit(3, little_endian = True)
circuit.hadamard(0)
circuit.cnot(0,1)
circuit.t(2)
```

### _ _operator_matrix_ _(gate_matrix: np.array, qubit: int, double: bool = False):
##### Returns the tensor product of the desired gates, see method itself for more information.

### amplitude(round: int = 3):
##### Returns an array of values to signify the amplitude of each and every value possible from the state.

### phaseAngle(round: int = 2):
##### Returns the radian value for each and every possible value within the state it is being applied to.

### state(round: int = 3):
##### Returns the initial state values within a vector state.

### probabilities(round: int = 3):
##### Returns all probabilities from the possible values found within the state.
### measure():
###### Returns the measurement of the state and will result in a random collapsing.
### cnot(control: int, target: int):
##### Calls the CNOT gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### x(qubit: int):
##### Calls the PauliX gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### y(qubit: int):
##### Calls the PauliY gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### z(qubit: int):
##### Calls the PauliZ gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### swap(qubit_1: int, qubit_2: int):
##### Calls the SWAP gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### toffoli(control_1: int, control_2: int, target: int):
##### Calls the TOFFOLI gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### phase(qubit: int, theta: float = np.pi / 2):
##### Calls the Phase gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### hadamard(qubit: int):
##### Calls the Hadamard gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### s(qubit: int):
##### Calls the S gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### sdg(qubit: int):
##### Calls the SDG gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### t(qubit: int):
##### Calls the T gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### tdg(qubit: int):
##### Calls the TDG gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### rz(qubit: int):
##### Calls the RZ gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### rx(qubit: int):
##### Calls the RX gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### ry(qubit: int):
##### Calls the RY gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### sx(qubit: int):
##### Calls the SX gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### sxdg(qubit: int):
##### Calls the SXDG gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### u(qubit: int, theta: float = np.pi / 2, phi: float = np.pi / 2, lbmda: float = np.pi / 2):
##### Calls the U gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### rxx(qubit_1: int, qubit_2: int, theta: float = np.pi / 2):
##### Calls the RXX gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.
### rzz(qubit_1: int, qubit_2: int, theta: float = np.pi / 2):
##### Calls the RZZ gate from the QuatumGate.py file to be interpreted into the __operator_matrix__ method.

## Visualizer.py
###### A collection of classes to visualize the quantum circuit

'''
circuit = QuantumCircuit(3, little_endian = True)
circuit.hadamard(0)
circuit.hadamard(1)
circuit.hadamard(2)
circuit.cnot(0,1)

test = Probabilities(circuit)
test.makeGraph(save=True, show=True, darkmode=True)

test = StateVector(circuit)
test.makeGraph(save=True, show=True, darkmode=True)
'''

#### StateVector
###### The amplitudes of the quantum circuit visualized as a graph
### makeGraph(self, path: str = "statevector.png", save: bool = True, show: bool = False, darkmode: bool = True)

#### Probabilities
###### The probabilities of each state being measured visualized as a graph
### makeGraph(self, path: str = "probabilities.png", save: bool = True, show: bool = False, darkmode: bool = True)
