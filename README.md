# README.md

# QCpy - A Quantum Computing Library for Python

QCpy is an open source python library and collaborative project for flexible simulations and visualizations of quantum circuits. Designed by college students with students in mind, this library contains a powerful set of tools to teach computer scientists about the emerging discipline of quantum computing (QC).

## Recommended Resources on Quantum Computing:

- [Microsoft’s Linear Algebra for Quantum Computing](https://learn.microsoft.com/en-us/azure/quantum/overview-algebra-for-quantum-computing)
- [IBM’s Quantum Computing: a field guide](https://quantum-computing.ibm.com/composer/docs/iqx/guide/)
- [Wikipedia: Quantum Computing](https://en.wikipedia.org/wiki/Quantum_computing)

---

# Qubits

> ## *class* QC.Qubit.`Qubit`(*initial_state=’z’*)

*Object representation of a qubit.*

### Parameters:

`initial_state (chr)` - Character input for starting direction in the *x*, *y*, or *z* axis.

### Attributes:

`state (numpy.ndarray)` -  current state of qubit in matrix representation.

---

# Quantum Gates

> ## *class* QC.QuantumGate.`Identity`()

*Gate that does not modify the quantum state.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Identity gate.

```python
Identity.matrix = [1+0j, 0+0j], 
	          [0+0j, 1+0j]
```

> ## *class* QC.QuantumGate.`PauliX`()

*Quantum equivalent of the NOT gate in classical computing with respect to the standard basis |0>, |1>.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Pauli-X gate.

```python
PauliX.matrix = [0+0j, 1+0j], 
	        [1+0j, 0+0j]
```

> ## *class* QC.QuantumGate.`PauliY`()

*Rotation around y-axis of the bloch sphere by π radiains, mapping |0> to i|1> and |1> to -i|0>.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Pauli-Y gate.

```python
PauliY.matrix = [0+0j, 0-1j],
                [0+1j, 0+0j]
```

> ## *class* QC.QuantumGate.`PauliZ`()

*Rotation around z-axis of the bloch sphere by π radiains, mapping |1> to -|1>; known as the phase-flip.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Pauli-Z gate.

```python
PauliY.matrix = [1+0j, 0+0j], 
                [0+0j, -1+0j]
```

> ## *class* QC.QuantumGate.`Hadamard`()

*Maps the basis states |0> to |+> and |1> to |->, creating a superposition state if given a computation basis state.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Hadamard gate.

```python
Hadamard.matrix = ([1,  1] 
                   [1, -1]) * (1/sqrt(2))
```

> ## *class* QC.QuantumGate.`CNot`(*inverse=False*)

*Controlled gate acts on two or more qubits, performing the NOT operation of the target qubit only if the control qubits are |1>, can act as a quantum regiester and is used to entangle and disentangle Bell states.*

### Parameters:

`inverse (bool)` - if the gate is an inverse, with the target being above the control.

### Attributes:

`matrix (np.ndarray)` - matrix representation of CNOT gate.

```python
# regular
CNot.matrix = [1+0j, 0+0j, 0+0j, 0+0j],
              [0+0j, 1+0j, 0+0j, 0+0j],
              [0+0j, 0+0j, 0+0j, 1+0j],
              [0+0j, 0+0j, 1+0j, 0+0j]
# inverse
CNot.matrix = [1+0j, 0+0j, 0+0j, 0+0j],
              [0+0j, 0+0j, 0+0j, 1+0j],
              [0+0j, 0+0j, 1+0j, 0+0j],
              [0+0j, 1+0j, 0+0j, 0+0j] 
```

> ## *class* QC.QuantumGate.`Swap`()

*Swaps two qubits, with respect to the basis |00>, |01>, |10>, and |11>.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of SWAP gate.

```python
Swap.matrix = [1+0j, 0+0j, 0+0j, 0+0j],
              [0+0j, 0+0j, 1+0j, 0+0j],
              [0+0j, 1+0j, 0+0j, 0+0j],
              [0+0j, 0+0j, 0+0j, 1+0j]
```

> ## *class* QC.QuantumGate.`Toffoli`()

*Universal reversible logic gate, known as the “controlled-controlled-NOT” gate; if the two control bits are set to 1, it will invert the target.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Toffoli gate.

```python
Toffoli.matrix = [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
                 [0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
                 [0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
                 [0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j],
                 [0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j],
                 [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j],
                 [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j],
                 [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j]
```

> ## *class* QC.QuantumGate.`Phase`(*theta=numpy.pi/2*)

*Applies a rotation of theta around the z-axis.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

### Attributes:

`matrix (np.ndarray)` - matrix representation of Phase gate.

```python
Phase.matrix = [1+0j, 0+0j],
	       [0+0j, numpy.exp(0+1j * theta)]
```

> ## *class* QC.QuantumGate.`S`()

*Equivalent to a pi/2 rotation around the z-axis.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of S gate.

```python
S.matrix = [1+0j, 0+0j],
           [0+0j, 0+1j]
```

> ## *class* QC.QuantumGate.`Sdg`()

*Inverse of S gate; a -pi/2 rotation around the z-axis.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of an inverse S gate.

```python
Sdg.matrix = [1+0j, 0+0j],
             [0+0j, 0-1j]
```

> ## *class* QC.QuantumGate.`T`()

*Square of S gate; where T = S^2.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of a T gate.

```python
T.matrix = [1+0j, 0+0j],
           [0+0j, numpy.exp((0+1j * numpy.pi) / 4)]
```

> ## *class* QC.QuantumGate.`Tdg`()

*Inverse of T gate.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of a inverse of T gate.

```python
Tdg.matrix = [1+0j, 0+0j],
             [0+0j, numpy.exp((0-1j * numpy.pi) / 4)]
```

> ## *class* QC.QuantumGate.`Rz`(*theta=numpy.pi/2*)

*Rotation of qubit around the z-axis.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Rz gate.

```python
Rz.matrix = [numpy.exp((0-1j * (theta / 2))), 0+0j],
            [0+0j, numpy.exp(0+1j * (theta / 2))]
```

> ## *class* QC.QuantumGate.`Rx`(*theta=numpy.pi/2*)

*Rotation of qubit around the x-axis.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around x-axis.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Rx gate.

```python
Rx.matrix = [numpy.cos(theta / 2), 0-1j * numpy.sin(theta / 2)],
            [0-1j * numpy.sin(theta / 2), numpy.cos(theta / 2)]
```

> ## *class* QC.QuantumGate.`Ry`(*theta=numpy.pi/2*)

*Rotation of qubit around the y-axis.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around y-axis.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Ry gate.

```python
Ry.matrix = [numpy.cos(theta / 2), -1 * numpy.sin(theta / 2)],
            [numpy.sin(theta / 2), numpy.cos(theta / 2)]
```

> ## *class* QC.QuantumGate.`Sx`()

*Rotation around the x-axis by 90 degrees in the counter-clockwise direction. Also known as the “square-root X gate” due to the fact that applying the SX gate twice results in an X gate.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Sx gate.

```python
Sx.matrix = [1+1j, 1-1j], 
            [1-1j, 1+1j]]) * (1 / 2)
```

> ## *class* QC.QuantumGate.`Sxdg`()

*Inverse of the Sx gate.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of an inverse Sx gate.

```python
Sxdg.matrix = [1-1j, 1+1j], 
              [1+1j, 1-1j]]) * (1 / 2)
```

> ## *class* QC.QuantumGate.`U`(*theta=numpy.pi/2, phi=numpy.pi/2, lmbda=numpy.pi/2*)

*Rotation of qubit with respect to theta, phi, and lambda, in Euler angles.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around Euler angle theta.

`phi (float)` default: `numpy.pi/2` -  angle of rotation around Euler angle phi.

`lmbda (float)` default: `numpy.pi/2` -  angle of rotation around Eulear angle lambda.

### Attributes:

`matrix (np.ndarray)` - matrix representation of a U gate.

```python
U.matrix = [numpy.cos(theta / 2), -1 * numpy.exp(0+1j * lmbda) * numpy.sin(theta / 2)], 
           [numpy.exp(0+1j * phi) * numpy.sin(theta / 2), numpy.exp(0+1j * (lmbda + phi)) * numpy.cos(theta / 2)]]
```

> ## *class* QC.QuantumGate.`Rxx`(*theta=numpy.pi/2*)

*Rotation about XX, maximally entangling at theta = pi/2.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around XX.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Rxx gate.

```python
Rxx.matrix = [numpy.cos(theta / 2), 0+0j, 0+0j, 0-1j * numpy.sin(theta / 2)],
             [0+0j, numpy.cos(theta / 2), 0-1j * numpy.sin(theta / 2), 0+0j],
             [0+0j, 0-1j * numpy.sin(theta / 2), numpy.cos(theta / 2), 0+0j],
             [0-1j * numpy.sin(theta / 2), 0+0j, 0+0j, numpy.cos(theta / 2)]
```

> ## *class* QC.QuantumGate.`Rzz`(*theta=numpy.pi/2*)

*Rotation about ZZ, maximally entangling at theta = pi/2.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around ZZ.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Rzz gate.

```python
Rzz.matrix = [numpy.exp(0-1j * (theta / 2)), 0+0j, 0+0j, 0+0j],
             [0+0j, numpy.exp(0+1j * (theta / 2)), 0+0j, 0+0j],
             [0+0j, 0+0j, numpy.exp(0+1j * (theta / 2)), 0+0j],
             [0+0j, 0+0j, 0+0j, numpy.exp(0-1j * (theta / 2))]
```

> ## *class* QC.QuantumGate.`Cr`(*theta=numpy.pi/2*)

*Controlled phase shift rotation in theta radians; generalization of Cz gate.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation in theta radians.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Cr gate.

```python
Cz.matrix = [1+0j, 0+0j, 0+0j, 0+0j],
            [0+0j, 1+0j, 0+0j, 0+0j],
            [0+0j, 0+0j, 1+0j, 0+0j],
            [0+0j, 0+0j, 0+0j, numpy.exp(theta * 0+1j)]
```

> ## *class* QC.QuantumGate.`Cz`(*theta=numpy.pi/2*)

*Controlled phase shift rotation in theta radians.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation in theta radians.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Cz gate.

```python
Cz.matrix = [1+0j, 0+0j, 0+0j, 0+0j],
            [0+0j, 1+0j, 0+0j, 0+0j],
            [0+0j, 0+0j, 1+0j, 0+0j],
            [0+0j, 0+0j, 0+0j, -1+0j]
```
---
# Quantum Circuit
> ## *class* QC.QuantumCircuit.`QuantumCircuit`(*qubits*, *little_endian=False*, *prep='z'*)

*Quantum circuit that represents the state of a quantum system and performs operations on select qubits.*

### Parameters:

`qubits (int)` - number of qubits in the circuit.

`little_endian (bool)` default: `False` - order of qubits and tensor products.

`prep (char)` options: [`z`, `y`, `x`] - initial direction of the qubits' phase angle.

### Attributes:

`None`

> ## QuantumCircuit.`circuit`()

*Dictionary representation of the circuit*

### Parameters:

`None`

### Returns:

`circuit (dict[int, list[str]])` - key: qubit; value: name of gate.

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)
qc.cnot(0, 1)
qc.hadamard(0)

print(qc.circuit())

# {0: ['hadamard', 'cnot_control', 'hadamard'], 
#  1: ['cnot_target']}
```

> ## QuantumCircuit.`amplitude`(*round=3*)

*Returns vector of all possible amplitudes for the quantum circuit*

### Parameters:

`round (int)` - rounding the amplitude to the nearest `round`

### Returns:

`amplitude (numpy.ndarray[float16])` - amplitude of the quantum circuit.

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)
qc.cnot(0, 1)
qc.hadamard(0)

print(qc.amplitude())

# [[0.5]
# [0.5]
# [0.5]
# [0.5]]
```

> ## QuantumCircuit.`phaseAngle`(*round=2*, *radian=True*)

*Calculates possible phase angles for the quantum circuit*

### Parameters:

`round (int)` - rounding the amplitude to the nearest `round`

`radian (bool)` - whether or not the values are in radians or degrees.

### Returns:

`phase_angle (numpy.ndarray)` - array of qubit's phase angle.

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)
qc.cnot(0, 1)
qc.hadamard(0)

print(qc.phaseAngle())

# [[0.        ]
# [0.         ]
# [0.         ]
# [3.14159265]]
```

> ## QuantumCircuit.`state`(*round=3*)

*Returns state of the quantum circuit.*

### Parameters:

`round (int)` - rounding the state to the nearest `round`

### Returns:

`_state (numpy.ndarray)` - array of quantum circuit's state.

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)
qc.cnot(0, 1)

print(qc.state())

# [[0.707+0.j]
# [0.   +0.j]
# [0.   +0.j]
# [0.707+0.j]]
```

> ## QuantumCircuit.`probabilities`(*round=3*)

*Returns probabilitiy of the qubits within the quantum circuit.*

### Parameters:

`round (int)` - rounding the probabilities to the nearest `round`

### Returns:

`prob_matrix (numpy.ndarray)` - array of quantum circuit's probabilities.

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.cnot(0, 1)

print(qc.probabilities())

# [0.5 0.  0.  0.5]
```

> ## QuantumCircuit.`measure`()

*Collapses the state based on the quantum circuit's probabilities.*

### Parameters:

`None`

### Returns:

`final_state (numpy.ndarray)` - array of quantum circuit's measurement.

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)
qc.cnot(0, 1)

print(qc.measure())

# ~Results may vary~
# 00
```

> ## QuantumCircuit.`reverse`()

*Reverses the quantum circuit's values.*

### Parameters:

`None`

### Returns:

`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

print(qc.state())

qc.reverse()

print(qc.state())

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
 
# [[0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]]
```
> ## QuantumCircuit.`toffoli`(*control_1*, *control_2*, *target*)

*A 3-qubit quantum gate that takes in two control qubits and one target qubit.*

### Parameters:

`control_1 (int)` - first control qubit.

`control_2 (int)` - second control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(3)

qc.hadamard(0)

qc.hadamard(1)

qc.toffoli(0,1,2)

print(qc.state())

# [[0.5+0.j]
# [0. +0.j]
# [0.5+0.j]
# [0. +0.j]
# [0.5+0.j]
# [0. +0.j]
# [0. +0.j]
# [0.5+0.j]]
```

> ## QuantumCircuit.`rccx`(*control_1*, *control_2*, *target*)

*A 3-qubit quantum gate that takes in two control qubits and one target qubit.*

### Parameters:

`control_1 (int)` - first control qubit.

`control_2 (int)` - second control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit
qc = QuantumCircuit(3)

qc.hadamard(0)

qc.hadamard(1)

qc.rccx(0,1,2)

print(qc.state())

# [[ 0.5-0.j ]
# [ 0. +0.j ]
# [ 0.5-0.j ]
# [ 0. +0.j ]
# [ 0.5-0.j ]
# [ 0. +0.j ]
# [-0. +0.j ]
# [ 0. +0.5j]]
```

> ## QuantumCircuit.`rc3x`(*a*, *b*, *c*, *d*)

*A 4-qubit quantum gate that takes in 4 unique qubits.*

### Parameters:

`a (int)` - first input qubit.

`b (int)` - second input qubit.

`c (int)` - third input qubit.

`d (int)` - fourth input qubit.


### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit
qc = QuantumCircuit(4)

qc.hadamard(0)

qc.hadamard(1)

qc.hadamard(2)

qc.rc3x(0,1,2)

print(qc.state())

# [[ 0.354-0.j   ]
# [ 0.   +0.j   ]
# [ 0.354-0.j   ]
# [ 0.   +0.j   ]
# [ 0.354-0.j   ]
# [ 0.   +0.j   ]
# [ 0.354-0.j   ]
# [ 0.   +0.j   ]
# [ 0.354-0.j   ]
# [ 0.   +0.j   ]
# [ 0.354-0.j   ]
# [ 0.   +0.j   ]
# [ 0.   +0.354j]
# [-0.   +0.j   ]
# [ 0.   -0.j   ]
# [-0.354+0.j   ]]
```
> ## QuantumCircuit.`cnot`(*control*, *target*)

*A 2-qubit quantum gate that takes in a control qubit and one target qubit.*

### Parameters:

`control (int)` - control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit
qc = QuantumCircuit(2)

qc.hadamard(0)

qc.cnot(0,1)

print(qc.state())

# [[0.707+0.j]
# [0.   +0.j]
# [0.   +0.j]
# [0.707+0.j]]
```

> ## QuantumCircuit.`cr`(*control*, *target*)

*A 2-qubit quantum gate that takes in a control qubit and one target qubit.*

### Parameters:

`control (int)` - control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit
qc = QuantumCircuit(2)

qc.hadamard(0)

qc.cr(0,1)

print(qc.state())

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
```


> ## QuantumCircuit.`cz`(*control*, *target*)

*A 2-qubit quantum gate that takes in a control qubit and one target qubit.*

### Parameters:

`control (int)` - control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit
qc = QuantumCircuit(2)

qc.hadamard(0)

qc.cz(0,1)

print(qc.state())

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
```

> ## QuantumCircuit.`swap`(*qubit_1*, *qubit_2*)

*A 2-qubit quantum gate that takes in 2 qubits to swap there properties.*

### Parameters:

`qubit_1 (int)` - first qubit to swap.

`qubit_2 (int)` - second qubit to swap.


### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit
qc = QuantumCircuit(2)

qc.hadamard(0)

qc.swap(0,1)

print(qc.state())

# [[0.707+0.j]
# [0.707+0.j]
# [0.   +0.j]
# [0.   +0.j]]
```

> ## QuantumCircuit.`rxx`(*qubit_1*, *qubit_2*, *theta=numpy.pi/2*)

*A 2-qubit quantum gate that takes in two qubits and a representation of theta to initialize in the quantum state.*

### Parameters:

`qubit_1 (int)` - first qubit input.

`qubit_2 (int)` - second qubit input.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit
qc = QuantumCircuit(2)

qc.hadamard(0)

qc.rxx(0,1)

print(qc.state())

# [[0.5+0.j ]
# [0. -0.5j]
# [0.5+0.j ]
# [0. -0.5j]]
```

> ## QuantumCircuit.`rzz`(*qubit_1*, *qubit_2*, *theta=numpy.pi/2*)

*A 2-qubit quantum gate that takes in two qubits and a representation of theta to initialize in the quantum state.*

### Parameters:

`qubit_1 (int)` - first qubit input.

`qubit_2 (int)` - second qubit input.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.


### Returns:
`None`

### Example:

```python
from QCpy.QuantumCircuit import QuantumCircuit
qc = QuantumCircuit(2)

qc.hadamard(0)

qc.rxx(0,1)

print(qc.state())

# [[0.5+0.j ]
# [0. -0.5j]
# [0.5+0.j ]
# [0. -0.5j]]
```

> ## QuantumCircuit.`customControlPhase`(*control*, *target*, *custom_matrix*)

*Used to insert single qubit based quantum gates to have a control qubit apart of it and committing to the quantum state.*

### Parameters:

`control (int)` - control qubit for given matrix.

`target (int)` - target qubit for given matrix.

`custom_matrix (np.array)` -  matrix to be applied to the quantum circuit.


### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

from QuantumGate import PauliX

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.customControlPhase(0,1, PauliX().matrix)

print(qc.state())

# [[0.707+0.j]
# [0.   +0.j]
# [0.   +0.j]
# [0.707+0.j]]
```

> ## QuantumCircuit.`identity`(*qubit*)

*Used to confirm value that a qubit is representing and does nothing to manipulate the value of such qubit.*

### Parameters:

`qubit (int)` - the qubit to have the identity gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.identity(0)

print(qc.state())

# [[1.+0.j]
# [0.+0.j]
# [0.+0.j]
# [0.+0.j]]
```

> ## QuantumCircuit.`x`(*qubit*)

*Used to invert the value of what a qubit is representing.*

### Parameters:

`qubit (int)` - the qubit to have the Pauli-X gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.x(0)

print(qc.state())

# [[0.+0.j]
# [0.+0.j]
# [1.+0.j]
# [0.+0.j]]
```


> ## QuantumCircuit.`hadmard`(*qubit*)

*Used to put a given qubit into superposition.*

### Parameters:

`qubit (int)` - the qubit to have the Hadamard gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

print(qc.state())

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
```

> ## QuantumCircuit.`y`(*qubit*)

*Changes the state of a qubit by pi around the y-axis of a Bloch Sphere.*

### Parameters:

`qubit (int)` - the qubit to have the Pauli-Y gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.y(0)

print(qc.state())

# [[0.+0.j]
# [0.+0.j]
# [0.+1.j]
# [0.+0.j]]
```


> ## QuantumCircuit.`z`(*qubit*)

*Changes the state of a qubit by pi around the z-axis of a Bloch Sphere.*

### Parameters:

`qubit (int)` - the qubit to have the Pauli-Z gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.z(0)

print(qc.state())

# [[ 0.707+0.j]
# [ 0.   +0.j]
# [-0.707+0.j]
# [ 0.   +0.j]]
```

> ## QuantumCircuit.`phase`(*qubit*, *theta=numpy.pi/2*)

*Commits to a rotation around the z-axis based off of the inputted theta value.*

### Parameters:

`qubit (int)` - the qubit to have the Phase gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.phase(0)

print(qc.state())

# [[0.707+0.j   ]
# [0.   +0.j   ]
# [0.   +0.707j]
# [0.   +0.j   ]]
```

> ## QuantumCircuit.`s`(*qubit*)

*Is a Phase gate where the inputted theta value is given as a constant of theta = pi / 2.*

### Parameters:

`qubit (int)` - the qubit to have the Pauli-Z gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.s(0)

print(qc.state())

# [[0.707+0.j   ]
# [0.   +0.j   ]
# [0.   +0.707j]
# [0.   +0.j   ]]
```

> ## QuantumCircuit.`sdg`(*qubit*)

*Is a Phase gate and inverse of the S gate where the inputted theta value is given as a constant of theta = -pi / 2.*

### Parameters:

`qubit (int)` - the qubit to have the Sdg gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.sdg(0)

print(qc.state())

# [[0.707+0.j   ]
# [0.   +0.j   ]
# [0.   -0.707j]
# [0.   +0.j   ]]
```

> ## QuantumCircuit.`t`(*qubit*)

*T gate is a special use case gate that in implemented from the P Gate.*

### Parameters:

`qubit (int)` - the qubit to have the T gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.t(0)

print(qc.state())

# [[0.707+0.j ]
# [0.   +0.j ]
# [0.5  +0.5j]
# [0.   +0.j ]]
```

> ## QuantumCircuit.`tdg`(*qubit*)

*Tdg gate is a special use case gate that in implemented from the P Gate and is the inverse of the T gate.*

### Parameters:

`qubit (int)` - the qubit to have the Tdg gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.tdg(0)

print(qc.state())

# [[0.707+0.j ]
# [0.   +0.j ]
# [0.5  -0.5j]
# [0.   +0.j ]]
```

> ## QuantumCircuit.`rz`(*qubit*, *theta=numpy.pi/2*)

*RZ gate commits a rotation around the z-axis for a qubit.*

### Parameters:

`qubit (int)` - the qubit to have the Rz gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.hadamard(0)

qc.rz(0)

print(qc.state())

# [[0.5-0.5j]
# [0. +0.j ]
# [0.5+0.5j]
# [0. +0.j ]]
```

> ## QuantumCircuit.`ry`(*qubit*, *theta=numpy.pi/2*)

*RY gate commits a rotation around the y-axis for a qubit.*

### Parameters:

`qubit (int)` - the qubit to have the Ry gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around y-axis.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.ry(0)

print(qc.state())

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
```

> ## QuantumCircuit.`rx`(*qubit*, *theta=numpy.pi/2*)

*RX gate commits a rotation around the x-axis for a qubit.*

### Parameters:

`qubit (int)` - the qubit to have the Ry gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around x-axis.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.rx(0)

print(qc.state())

# [[0.707+0.j   ]
# [0.   +0.j   ]
# [0.   -0.707j]
# [0.   +0.j   ]]
```

> ## QuantumCircuit.`sx`(*qubit*)

*SX gate is the square root of the Inverse gate (X, PauliX Gate).*

### Parameters:

`qubit (int)` - the qubit to have the Sx gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.sx(0)

print(qc.state())

# [[0.5+0.5j]
# [0. +0.j ]
# [0.5-0.5j]
# [0. +0.j ]]
```

> ## QuantumCircuit.`sxdg`(*qubit*)

*SXDG gate is the negative square root of the Inverse gate (X, PauliX Gate) and inverse of the SX gate.*

### Parameters:

`qubit (int)` - the qubit to have the SXdg gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.sxdg(0)

print(qc.state())

# [[0.5-0.5j]
# [0. +0.j ]
# [0.5+0.5j]
# [0. +0.j ]]
```

> ## QuantumCircuit.`u`(*qubit*, *theta=numpy.pi/2*, *phi=numpy.pi/2*, *lmbda=numpy.pi/2*)

*U gate is given three inputs (theta, phi, and lambda) that allow the inputs to manipulate the base matrix to allow for the position of the enacted qubit around the bloch sphere representation.*

### Parameters:

`qubit (int)` - the qubit to have the U gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` - angle representation to rotate the qubit's representation.

`phi (float)` default: `numpy.pi/2` -  angle representation to rotate the qubit's representation.

`lmbda (float)` default: `numpy.pi/2` -  angle representation to rotate the qubit's representation.

### Returns:
`None`

### Example:

```python
from QuantumCircuit import QuantumCircuit

qc = QuantumCircuit(2)

qc.u(0)

print(qc.state())

# [[0.5-0.5j]
# [0. +0.j ]
# [0.5+0.5j]
# [0. +0.j ]]
```
