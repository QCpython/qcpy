# README.md

# QCpy - A Quantum Computing Library for Python

QCpy is an open source python library and collaborative project for flexible simulations and visualizations of quantum circuits. Designed by college students with students in mind, this library contains a powerful set of tools to teach computer scientists about the emerging discipline of quantum computing.

You can download the package using pip:

```txt
pip install qcpython
```
---

# Qubit

> ## qcpy.`qubit`(*initial_state=’z’*)

*Object representation of a qubit.*

### Parameters:

`initial_state (chr)` default: `z` - Character input for starting direction in the *x*, *y*, or *z* axis.

### Attributes:

`None`

### Example:

```python
from qcpy import qubit

qx = qubit(initial_state = 'x')
qy = qubit(initial_state = 'y')
qz = qubit(initial_state = 'z')
print("qx:\n", qx)
print("qy:\n", qy)
print("qz:\n", qz)


# qx:
#  [[0.70710677+0.j]
#  [0.70710677+0.j]]
# qy:
#  [[0.70710677+0.j]
#  [0.+0.70710677j]]
# qz:
#  [[1.+0.j]
#  [0.+0.j]]
```
---

# Quantum Gates

> ## quantumgate.`identity`()

*Gate that does not modify the quantum state.*

### Parameters:

`None`

```python
identity=[1+0j, 0+0j], 
         [0+0j, 1+0j]
```
### Example:

```python
from qcpy import identity 

print(identity())

# [[1.+0.j 0.+0.j]
#  [0.+0.j 1.+0.j]]
```
> ## quantumgate.`paulix`()

*Quantum equivalent of the NOT gate in classical computing with respect to the standard basis |0>, |1>.*

### Parameters:

`None`

```python
PauliX = [0+0j, 1+0j], 
	 [1+0j, 0+0j]
```
### Example:

```python
from qcpy import paulix

print(paulix())

# [[1.+0.j 0.+0.j]
#  [0.+0.j 1.+0.j]]
```
> ## quantumgate.`pauliy`()

*Rotation around y-axis of the bloch sphere by π radiains, mapping |0> to i|1> and |1> to -i|0>.*

### Parameters:

`None`

```python
PauliY = [0+0j, 0-1j],
         [0+1j, 0+0j]
```
### Example:

```python
from qcpy import pauliy

print(pauliy())

# [[0+0j, 0-1j]
#  [0+1j, 0+0j]]
```
> ## quantumgate.`pauliz`()

*Rotation around z-axis of the bloch sphere by π radiains, mapping |1> to -|1>; known as the phase-flip.*

### Parameters:

`None`

```python
PauliZ = [1+0j, 0+0j], 
         [0+0j, -1+0j]
```
### Example:

```python
from qcpy import pauliz

print(pauliz())

# [[1+0j, 0+0j], 
#  [0+0j, -1+0j]]
```
> ## quantumgate.`hadamard`()

*Maps the basis states |0> to |+> and |1> to |->, creating a superposition state if given a computation basis state.*

### Parameters:

`None`

```python
Hadamard = [1,  1] 
           [1, -1] * (1/sqrt(2))
```
### Example:

```python
from qcpy import hadamard

print(hadamard())

# [[ 0.70710677+0.j  0.70710677+0.j]
#  [ 0.70710677+0.j -0.70710677+0.j]]
```
> ## quantumgate.`cnot`(*little_endian=False*)

*Controlled gate acts on two or more qubits, performing the NOT operation of the target qubit only if the control qubits are |1>, can act as a quantum regiester and is used to entangle and disentangle Bell states.*

### Parameters:

`little_endian (bool)` - if the gate is an inverse, with the target being above the control.

```python
# regular
CNot = [1+0j, 0+0j, 0+0j, 0+0j],
       [0+0j, 1+0j, 0+0j, 0+0j],
       [0+0j, 0+0j, 0+0j, 1+0j],
       [0+0j, 0+0j, 1+0j, 0+0j]
# little_endian = True
CNot = [1+0j, 0+0j, 0+0j, 0+0j],
       [0+0j, 0+0j, 0+0j, 1+0j],
       [0+0j, 0+0j, 1+0j, 0+0j],
       [0+0j, 1+0j, 0+0j, 0+0j] 
```
### Example:

```python
from qcpy import cnot

print(cnot())

# [[1.+0.j 0.+0.j 0.+0.j 0.+0.j]
#  [0.+0.j 1.+0.j 0.+0.j 0.+0.j]
#  [0.+0.j 0.+0.j 0.+0.j 1.+0.j]
#  [0.+0.j 0.+0.j 1.+0.j 0.+0.j]]

# [[1.+0.j 0.+0.j 0.+0.j 0.+0.j]
#  [0.+0.j 0.+0.j 0.+0.j 1.+0.j]
#  [0.+0.j 0.+0.j 1.+0.j 0.+0.j]
#  [0.+0.j 1.+0.j 0.+0.j 0.+0.j]]
```
> ## quantumgate.`swap`()

*Swaps two qubits, with respect to the basis |00>, |01>, |10>, and |11>.*

### Parameters:

`None`

```python
Swap = [1+0j, 0+0j, 0+0j, 0+0j],
       [0+0j, 0+0j, 1+0j, 0+0j],
       [0+0j, 1+0j, 0+0j, 0+0j],
       [0+0j, 0+0j, 0+0j, 1+0j]
```
### Example:

```python
from qcpy import swap

print(swap())

# [1+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 1+0j, 0+0j],
# [0+0j, 1+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 1+0j]
```
> ## quantumgate.`toffoli`()

*Universal reversible logic gate, known as the “controlled-controlled-NOT” gate; if the two control bits are set to 1, it will invert the target.*

### Parameters:

`None`

```python
Toffoli = [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
          [0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
          [0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
          [0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j],
          [0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j],
          [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j],
          [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j],
          [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j]
```
### Example:

```python
from qcpy import toffoli

print(toffoli())

# [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j],
# [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j]
```
> ## quantumgate.`phase`(*theta=numpy.pi/2*)

*Applies a rotation of theta around the z-axis.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

```python
Phase = [1+0j, 0+0j],
	[0+0j, numpy.exp(0+1j * theta)]
```
### Example:

```python
from qcpy import phase

print(phase())

# [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j, 0+0j],
# [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j],
# [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j, 0+0j]
```
> ## quantumgate.`s`()

*Equivalent to a pi/2 rotation around the z-axis.*

### Parameters:

`None`

```python
S.matrix = [1+0j, 0+0j],
           [0+0j, 0+1j]
```
### Example:

```python
from qcpy import s

print(s())

# [1+0j, 0+0j],
# [0+0j, 0+1j]
```
> ## quantumgate.`sdg`()

*Inverse of S gate; a -pi/2 rotation around the z-axis.*

### Parameters:

`None`

```python
Sdg.matrix = [1+0j, 0+0j],
             [0+0j, 0-1j]
```
### Example:

```python
from qcpy import sdg

print(sdg())

# [1+0j, 0+0j],
# [0+0j, 0-1j]
```
> ## quantumgate.`t`()

*Square of S gate; where T = S^2.*

### Parameters:

`None`

```python
T.matrix = [1+0j, 0+0j],
           [0+0j, numpy.exp((0+1j * numpy.pi) / 4)]
```
### Example:

```python
from qcpy import t

print(t())

# [[1.+0.j 0.+0.j]
#  [0.+0.j 0.70710677+0.70710677j]]
```
> ## quantumgate.`tdg`()

*Inverse of T gate.*

### Parameters:

`None`

```python
Tdg = [1+0j, 0+0j],
      [0+0j, numpy.exp((0-1j * numpy.pi) / 4)]
```
### Example:

```python
from qcpy import tdg

print(tdg())

# [[1.+0.j 0.+0.j]
#  [0.+0.j 0.70710677-0.70710677j]]
```
> ## quantumgate.`rz`(*theta=numpy.pi/2*)

*Rotation of qubit around the z-axis.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

```python
Rz = [numpy.exp((0-1j * (theta / 2))), 0+0j],
     [0+0j, numpy.exp(0+1j * (theta / 2))]
```

> ## quantumgate.`rx`(*theta=numpy.pi/2*)

*Rotation of qubit around the x-axis.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around x-axis.

```python
Rx = [numpy.cos(theta / 2), 0-1j * numpy.sin(theta / 2)],
     [0-1j * numpy.sin(theta / 2), numpy.cos(theta / 2)]
```
### Example:

```python
from qcpy import rx

print(rx())

# [[0.70710677+0.j 0.-0.70710677j]
#  [0.-0.70710677j 0.70710677+0.j]]
```
> ## quantumgate.`ry`(*theta=numpy.pi/2*)

*Rotation of qubit around the y-axis.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around y-axis.

```python
Ry = [numpy.cos(theta / 2), -1 * numpy.sin(theta / 2)],
     [numpy.sin(theta / 2), numpy.cos(theta / 2)]
```
### Example:

```python
from qcpy import ry

print(ry())

# [[ 0.70710677+0.j -0.70710677+0.j]
#  [ 0.70710677+0.j  0.70710677+0.j]]
```
> ## quantumgate.`sx`()

*Rotation around the x-axis by 90 degrees in the counter-clockwise direction. Also known as the “square-root X gate” due to the fact that applying the SX gate twice results in an X gate.*

### Parameters:

`None`

```python
Sx = [1+1j, 1-1j], 
     [1-1j, 1+1j] * (1 / 2)
```
### Example:

```python
from qcpy import sx

print(sx())

# [[0.5+0.5j 0.5-0.5j]
#  [0.5-0.5j 0.5+0.5j]]
```
> ## quantumgate.`sxdg`()

*Inverse of the Sx gate.*

### Parameters:

`None`

```python
Sxdg = [1-1j, 1+1j], 
       [1+1j, 1-1j] * (1 / 2)
```
### Example:

```python
from qcpy import sxdg

print(sxdg())

# [[0.5-0.5j 0.5+0.5j]
#  [0.5+0.5j 0.5-0.5j]]
```
> ## quantumgate.`u`(*theta=numpy.pi/2, phi=numpy.pi/2, lmbda=numpy.pi/2*)

*Rotation of qubit with respect to theta, phi, and lambda, in Euler angles.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around Euler angle theta.

`phi (float)` default: `numpy.pi/2` -  angle of rotation around Euler angle phi.

`lmbda (float)` default: `numpy.pi/2` -  angle of rotation around Eulear angle lambda.

```python
U.matrix = [numpy.cos(theta / 2), -1 * numpy.exp(0+1j * lmbda) * numpy.sin(theta / 2)], 
           [numpy.exp(0+1j * phi) * numpy.sin(theta / 2), numpy.exp(0+1j * (lmbda + phi)) * numpy.cos(theta / 2)]]
```
### Example:

```python
from qcpy import u

print(u())

# [[0.7071+0.j -0.-0.7071j]
#  [0.+0.7071j -0.7071+0.j]]
```
> ## quantumgate.`rxx`(*theta=numpy.pi/2*)

*Rotation about XX, maximally entangling at theta = pi/2.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around XX.

```python
Rxx.matrix = [numpy.cos(theta / 2), 0+0j, 0+0j, 0-1j * numpy.sin(theta / 2)],
             [0+0j, numpy.cos(theta / 2), 0-1j * numpy.sin(theta / 2), 0+0j],
             [0+0j, 0-1j * numpy.sin(theta / 2), numpy.cos(theta / 2), 0+0j],
             [0-1j * numpy.sin(theta / 2), 0+0j, 0+0j, numpy.cos(theta / 2)]
```
### Example:

```python
from qcpy import rxx

print(rxx())

# [[0.70710677+0.j 0+0.j 0+0.j 0-0.70710677j]
#  [0+0.j 0.70710677+0.j 0-0.70710677j 0+0.j]
#  [0+0.j 0-0.70710677j 0.70710677+0.j 0+0.j]
#  [0-0.70710677j 0+0.j 0.+0.j 0.70710677+0.j]]
```
> ## quantumgate.`rzz`(*theta=numpy.pi/2*)

*Rotation about ZZ, maximally entangling at theta = pi/2.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation around ZZ.

```python
Rzz.matrix = [numpy.exp(0-1j * (theta / 2)), 0+0j, 0+0j, 0+0j],
             [0+0j, numpy.exp(0+1j * (theta / 2)), 0+0j, 0+0j],
             [0+0j, 0+0j, numpy.exp(0+1j * (theta / 2)), 0+0j],
             [0+0j, 0+0j, 0+0j, numpy.exp(0-1j * (theta / 2))]
```
### Example:

```python
from qcpy import rzz

print(rzz())

# [[0.70710677-0.70710677j 0+0.j 0+0.jn 0+0.j]
#  [0+0.j 0.70710677+0.70710677j 0+0.j 0+0.j]
#  [0+0.j 0+0.j 0.70710677+0.70710677j 0+0.j]
#  [0+0.j 0+0.j 0+0.j 0.70710677-0.70710677j]]
```
> ## quantumgate.`cr`(*theta=numpy.pi/2*)

*Controlled phase shift rotation in theta radians; generalization of Cz gate.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation in theta radians.

```python
Cr = [1+0j, 0+0j, 0+0j, 0+0j],
     [0+0j, 1+0j, 0+0j, 0+0j],
     [0+0j, 0+0j, 1+0j, 0+0j],
     [0+0j, 0+0j, 0+0j, exp(theta * 0+1j)]
```
### Example:

```python
from qcpy import cr

print(cr())

# [[1+0.j 0+0.j 0+0.j 0+0.j]
#  [0+0.j 1+0.j 0+0.j 0+0.j]
#  [0+0.j 0+0.j 1+0.j 0+0.j]
#  [0+0.j 0+0.j 0+0.j 0.5403023+0.84147096j]]
```
> ## quantumgate.`cz`(*theta=numpy.pi/2*)

*Controlled phase shift rotation in theta radians.*

### Parameters:

`theta (float)` default: `numpy.pi/2` -  angle of rotation in theta radians.

```python
Cz = [1+0j, 0+0j, 0+0j, 0+0j],
     [0+0j, 1+0j, 0+0j, 0+0j],
     [0+0j, 0+0j, 1+0j, 0+0j],
     [0+0j, 0+0j, 0+0j, -1+0j]
```
### Example:

```python
from qcpy import cz

print(cz())

# [[ 1.+0.j  0.+0.j  0.+0.j  0.+0.j]
#  [ 0.+0.j  1.+0.j  0.+0.j  0.+0.j]
#  [ 0.+0.j  0.+0.j  1.+0.j  0.+0.j]
#  [ 0.+0.j  0.+0.j  0.+0.j -1.+0.j]]
```
---
# Quantum Circuit
> ## *class* qcpy.`quantumcircuit`(*qubits: int*, *little_endian: bool=False*, *prep: char='z'*)

*Quantum circuit that represents the state of a quantum system and performs operations on select qubits.*

### Parameters:

`qubits (int)` - number of qubits in the circuit.

`little_endian (bool)` default: `False` - order of qubits and tensor products.

`prep (char)` options: [`z`, `y`, `x`] - initial direction of the qubits' phase angle.

### Attributes:

`state (numpy.ndarray)` -  current state of quantum circuit in matrix representation.


> ## quantumcircuit.`amplitude`(*round: int=3*)

*Returns vector of all possible amplitudes for the quantum circuit*

### Parameters:

`round (int)` - rounding the amplitude to the nearest `round`

### Returns:

`amplitude (numpy.ndarray[float16])` - amplitude of the quantum circuit.

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)
qc.cnot(0, 1)
qc.h(0)

print(qc.amplitude())

# [[0.5]
# [0.5]
# [0.5]
# [0.5]]
```

> ## quantumcircuit.`phaseangle`(*round: int=2*, *radian: bool=True*)

*Calculates possible phase angles for the quantum circuit*

### Parameters:

`round (int)` - round phase angle for readability.

`radian (bool)` - whether or not the values are in radians or degrees.

### Returns:

`phase_angle (numpy.ndarray)` - array of qubit's phase angle.

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)
qc.cnot(0, 1)
qc.h(0)

print(qc.phaseangle())

# [[0.        ]
# [0.         ]
# [0.         ]
# [3.14159265]]
```

> ## quantumcircuit.`state`

*Returns state of the quantum circuit.*

### Parameters:

`None`

### Returns:

`state (numpy.ndarray)` - array of quantum circuit's state.

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)
qc.cnot(0, 1)

print(qc.state)

# [[0.707+0.j]
# [0.   +0.j]
# [0.   +0.j]
# [0.707+0.j]]
```

> ## quantumcircuit.`flatten(round: int=3)`

*Returns state of the quantum circuit in a 1D array.*

### Parameters:

`round (int)` - round state for readability.

### Returns:

`state (numpy.ndarray)` - array of quantum circuit's state.

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)
qc.cnot(0, 1)

print(qc.flatten())

# [0.707+0.j 0.   +0.j 0.   +0.j 0.707+0.j]
```

> ## quantumcircuit.`circuitqueue()`

*Returns queue of gates on quantum circuit.*

### Parameters:

`None`

### Returns:
`queue (list)` - list of gates queued on quantum circuit.

### Example:

```python
from qcpy import quantumcircuit

qc = QuantumCircuit(4)

qc.x(0)
qc.x(1)
qc.x(2)
qc.rc3x(0, 1, 2, 3)

print(qc.circuitqueue())

# [('X', 0), ('X', 1), ('X', 2), ('U', 3), ('U', 3), ('cnot', 2, # 3), ('U', 3), ('U', 3), ('swap', 2, 3), ('swap', 1, 2), 
# ('swap', 1, 2), ('swap', 2, 3), ('cnot', 0, 3), ('U', 3),
# ('swap', 2, 3), ('swap', 2, 3), ('cnot', 1, 3), ('U', 3), 
# ('swap', 2, 3), ('swap', 1, 2), ('swap', 1, 2), ('swap', 2, 
# 3), ('cnot', 0, 3), ('U', 3), ('swap', 2, 3), ('swap', 2, 3),
#  ('cnot', 1, 3), ('U', 3), ('U', 3), ('U', 3), ('cnot', 2, 3),
#  ('U', 3), ('U', 3), ('rc3x', 0, 1, 2, 3)]
```

> ## quantumcircuit.`probabilities`(*show_percent: bool=False*, *show_bit=-1*, *round: int=3*)

*Returns probabilitiy of the qubits within the quantum circuit.*

### Parameters:

`show_percent (bool)` - convert probability to be shown in percentage.

`show_bit (int or str)` - get the probability of a single bit with a given string of binary or a integer.

`round (int)` - rounding the probabilities to the nearest `round`.

### Returns:

`prob_matrix (numpy.ndarray)` - array of quantum circuit's probabilities.

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

qc.cnot(0, 1)

print(qc.probabilities())

# [0.5 0.  0.  0.5]
```

> ## quantumcircuit.`measure`()

*Collapses the state based on the quantum circuit's probabilities.*

### Parameters:

`None`

### Returns:

`final_state (numpy.ndarray)` - array of quantum circuit's measurement.

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)
qc.cnot(0, 1)

print(qc.measure())

# 00
```

> ## quantumcircuit.`reverse`()

*Reverses the quantum circuit's values.*

### Parameters:

`None`

### Returns:

`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

print(qc.state)

qc.reverse()

print(qc.state)

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
 
# [[0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]]
```
> ## quantumcircuit.`toffoli`(*control_1: int*, *control_2: int*, *target: int*)

*A 3-qubit quantum gate that takes in two control qubits and one target qubit.*

### Parameters:

`control_1 (int)` - first control qubit.

`control_2 (int)` - second control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(3)

qc.h(0)

qc.h(1)

qc.toffoli(0,1,2)

print(qc.state)

# [[0.5+0.j]
# [0. +0.j]
# [0.5+0.j]
# [0. +0.j]
# [0.5+0.j]
# [0. +0.j]
# [0. +0.j]
# [0.5+0.j]]
```

> ## quantumcircuit.`rccx`(*control_1*, *control_2*, *target*)

*A 3-qubit quantum gate that takes in two control qubits and one target qubit.*

### Parameters:

`control_1 (int)` - first control qubit.

`control_2 (int)` - second control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit
qc = quantumcircuit(3)

qc.h(0)

qc.h(1)

qc.rccx(0,1,2)

print(qc.state)

# [[ 0.5-0.j ]
# [ 0. +0.j ]
# [ 0.5-0.j ]
# [ 0. +0.j ]
# [ 0.5-0.j ]
# [ 0. +0.j ]
# [-0. +0.j ]
# [ 0. +0.5j]]
```

> ## quantumcircuit.`rc3x`(*qubit_1: int*, *qubit_2: int*, *qubit_3: int*, *qubit_4: int*)

*A 4-qubit quantum gate that takes in 4 unique qubits.*

### Parameters:

`qubit_1 (int)` - first input qubit.

`qubit_2 (int)` - second input qubit.

`qubit_3 (int)` - third input qubit.

`qubit_4 (int)` - fourth input qubit.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit
qc = quantumcircuit(4)

qc.h(0)

qc.h(1)

qc.h(2)

qc.rc3x(0,1,2,3)

print(qc.state)

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
> ## quantumcircuit.`cnot`(*control: int*, *target: int*)

*A 2-qubit quantum gate that takes in a control qubit and one target qubit.*

### Parameters:

`control (int)` - control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit
qc = quantumcircuit(2)

qc.h(0)

qc.cnot(0,1)

print(qc.state)

# [[0.707+0.j]
# [0.   +0.j]
# [0.   +0.j]
# [0.707+0.j]]
```

> ## quantumcircuit.`cr`(*control: int*, *target: int*)

*A 2-qubit quantum gate that takes in a control qubit and one target qubit.*

### Parameters:

`control (int)` - control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit
qc = quantumcircuit(2)

qc.h(0)

qc.cr(0,1)

print(qc.state)

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
```


> ## quantumcircuit.`cz`(*control: int*, *target: int*)

*A 2-qubit quantum gate that takes in a control qubit and one target qubit.*

### Parameters:

`control (int)` - control qubit.

`target (int)` - target qubit.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit
qc = quantumcircuit(2)

qc.h(0)

qc.cz(0,1)

print(qc.state)

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
```

> ## quantumcircuit.`swap`(*qubit_1: int*, *qubit_2: int*)

*A 2-qubit quantum gate that takes in 2 qubits to swap there properties.*

### Parameters:

`qubit_1 (int)` - first qubit to swap.

`qubit_2 (int)` - second qubit to swap.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit
qc = quantumcircuit(2)

qc.h(0)

qc.swap(0,1)

print(qc.state)

# [[0.707+0.j]
# [0.707+0.j]
# [0.   +0.j]
# [0.   +0.j]]
```

> ## quantumcircuit.`rxx`(*qubit_1: int*, *qubit_2: int*, *theta: float=numpy.pi/2*)

*A 2-qubit quantum gate that takes in two qubits and a representation of theta to initialize in the quantum state.*

### Parameters:

`qubit_1 (int)` - first qubit input.

`qubit_2 (int)` - second qubit input.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit
qc = quantumcircuit(2)

qc.h(0)

qc.rxx(0,1)

print(qc.state)

# [[0.5+0.j ]
# [0. -0.5j]
# [0.5+0.j ]
# [0. -0.5j]]
```

> ## quantumcircuit.`rzz`(*qubit_1*, *qubit_2*, *theta=numpy.pi/2*)

*A 2-qubit quantum gate that takes in two qubits and a representation of theta to initialize in the quantum state.*

### Parameters:

`qubit_1 (int)` - first qubit input.

`qubit_2 (int)` - second qubit input.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit
qc = quantumcircuit(2)

qc.h(0)

qc.rxx(0,1)

print(qc.state)

# [[0.5+0.j ]
# [0. -0.5j]
# [0.5+0.j ]
# [0. -0.5j]]
```

> ## quantumcircuit.`customcontrolled`(*control: int*, *target: int*, *custom_matrix: np.array*)

*Used to insert single qubit based quantum gates to have a control qubit apart of it and committing to the quantum state.*

### Parameters:

`control (int)` - control qubit for given matrix.

`target (int)` - target qubit for given matrix.

`custom_matrix (np.array)` - (2,2) matrix to be applied to the quantum circuit.


### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit, paulix

qc = quantumcircuit(2)

qc.h(0)

qc.customcontrolled(0,1, paulix())

print(qc.state)

# [[0.707+0.j]
# [0.   +0.j]
# [0.   +0.j]
# [0.707+0.j]]
```

> ## quantumcircuit.`i`(*qubit: int*)

*Used to confirm value that a qubit is representing and does nothing to manipulate the value of such qubit.*

### Parameters:

`qubit (int)` - the qubit to have the identity gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.i(0)

print(qc.state)

# [[1.+0.j]
# [0.+0.j]
# [0.+0.j]
# [0.+0.j]]
```

> ## quantumcircuit.`x`(*qubit: int*)

*Used to invert the value of what a qubit is representing.*

### Parameters:

`qubit (int)` - the qubit to have the Pauli-X gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.x(0)

print(qc.state)

# [[0.+0.j]
# [0.+0.j]
# [1.+0.j]
# [0.+0.j]]
```


> ## quantumcircuit.`hadmard`(*qubit: int*)

*Used to put a given qubit into superposition.*

### Parameters:

`qubit (int)` - the qubit to have the Hadamard gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

print(qc.state)

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
```

> ## quantumcircuit.`y`(*qubit: int*)

*Changes the state of a qubit by pi around the y-axis of a Bloch Sphere.*

### Parameters:

`qubit (int)` - the qubit to have the Pauli-Y gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.y(0)

print(qc.state)

# [[0.+0.j]
# [0.+0.j]
# [0.+1.j]
# [0.+0.j]]
```


> ## quantumcircuit.`z`(*qubit: int*)

*Changes the state of a qubit by pi around the z-axis of a Bloch Sphere.*

### Parameters:

`qubit (int)` - the qubit to have the Pauli-Z gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

qc.z(0)

print(qc.state)

# [[ 0.707+0.j]
# [ 0.   +0.j]
# [-0.707+0.j]
# [ 0.   +0.j]]
```

> ## quantumcircuit.`phase`(*qubit: int*, *theta: float=numpy.pi/2*)

*Commits to a rotation around the z-axis based off of the inputted theta value.*

### Parameters:

`qubit (int)` - the qubit to have the Phase gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

qc.phase(0)

print(qc.state)

# [[0.707+0.j   ]
# [0.   +0.j   ]
# [0.   +0.707j]
# [0.   +0.j   ]]
```

> ## quantumcircuit.`s`(*qubit: int*)

*Is a Phase gate where the inputted theta value is given as a constant of theta = pi / 2.*

### Parameters:

`qubit (int)` - the qubit to have the Pauli-Z gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

qc.s(0)

print(qc.state)

# [[0.707+0.j   ]
# [0.   +0.j   ]
# [0.   +0.707j]
# [0.   +0.j   ]]
```

> ## quantumcircuit.`sdg`(*qubit: int*)

*Is a Phase gate and inverse of the S gate where the inputted theta value is given as a constant of theta = -pi / 2.*

### Parameters:

`qubit (int)` - the qubit to have the Sdg gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

qc.sdg(0)

print(qc.state)

# [[0.707+0.j   ]
# [0.   +0.j   ]
# [0.   -0.707j]
# [0.   +0.j   ]]
```

> ## quantumcircuit.`t`(*qubit: int*)

*T gate is a special use case gate that in implemented from the P Gate.*

### Parameters:

`qubit (int)` - the qubit to have the T gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

qc.t(0)

print(qc.state)

# [[0.707+0.j ]
# [0.   +0.j ]
# [0.5  +0.5j]
# [0.   +0.j ]]
```

> ## quantumcircuit.`tdg`(*qubit: int*)

*Tdg gate is a special use case gate that in implemented from the P Gate and is the inverse of the T gate.*

### Parameters:

`qubit (int)` - the qubit to have the Tdg gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

qc.tdg(0)

print(qc.state)

# [[0.707+0.j ]
# [0.   +0.j ]
# [0.5  -0.5j]
# [0.   +0.j ]]
```

> ## quantumcircuit.`rz`(*qubit: int*, *theta: float=numpy.pi/2*)

*RZ gate commits a rotation around the z-axis for a qubit.*

### Parameters:

`qubit (int)` - the qubit to have the Rz gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around z-axis.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.h(0)

qc.rz(0)

print(qc.state)

# [[0.5-0.5j]
# [0. +0.j ]
# [0.5+0.5j]
# [0. +0.j ]]
```

> ## quantumcircuit.`ry`(*qubit: int*, *theta: float=numpy.pi/2*)

*RY gate commits a rotation around the y-axis for a qubit.*

### Parameters:

`qubit (int)` - the qubit to have the Ry gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around y-axis.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.ry(0)

print(qc.state)

# [[0.707+0.j]
# [0.   +0.j]
# [0.707+0.j]
# [0.   +0.j]]
```

> ## quantumcircuit.`rx`(*qubit: int*, *theta: float=numpy.pi/2*)

*RX gate commits a rotation around the x-axis for a qubit.*

### Parameters:

`qubit (int)` - the qubit to have the Ry gate be applied to the quantum wire.

`theta (float)` default: `numpy.pi/2` -  angle of rotation around x-axis.

### Returns:
`None`

### Example:

```python
from qcpy import quantumCircuit

qc = quantumcircuit(2)

qc.rx(0)

print(qc.state)

# [[0.707+0.j   ]
# [0.   +0.j   ]
# [0.   -0.707j]
# [0.   +0.j   ]]
```

> ## quantumcircuit.`sx`(*qubit: int*)

*SX gate is the square root of the Inverse gate (X, PauliX Gate).*

### Parameters:

`qubit (int)` - the qubit to have the Sx gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.sx(0)

print(qc.state)

# [[0.5+0.5j]
# [0. +0.j ]
# [0.5-0.5j]
# [0. +0.j ]]
```

> ## quantumcircuit.`sxdg`(*qubit: int*)

*SXDG gate is the negative square root of the Inverse gate (X, PauliX Gate) and inverse of the SX gate.*

### Parameters:

`qubit (int)` - the qubit to have the SXdg gate be applied to the quantum wire.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.sxdg(0)

print(qc.state)

# [[0.5-0.5j]
# [0. +0.j ]
# [0.5+0.5j]
# [0. +0.j ]]
```

> ## quantumcircuit.`u`(*qubit: int*, *theta: float=numpy.pi/2*, *phi: float=numpy.pi/2*, *lmbda: float=numpy.pi/2*)

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
from qcpy import quantumcircuit

qc = quantumcircuit(2)

qc.u(0)

print(qc.state)

# [[0.5-0.5j]
# [0. +0.j ]
# [0.5+0.5j]
# [0. +0.j ]]
```

> ## quantumcircuit.`custom`(*qubit: int*, *custom_matrix: np.array*)

*Will take in a custom single qubit quantum gate and implement it on a qubit.*

### Parameters:

`qubit (int)` - the qubit to have the U gate be applied to the quantum wire.

`custom_matrix (np.array)` -  matrix to be applied to the quantum circuit.

### Returns:
`None`

### Example:

```python
from qcpy import quantumcircuit, paulix

qc = quantumcircuit(2)

qc.custom(0, paulix())

print(qc.state)

# [[0.+0.j]
# [0.+0.j]
# [1.+0.j]
# [0.+0.j]]
```

# Visualizer

*A collection of classes to visualize the quantum circuit*

> ## *class* qcpy.qsphere(*circuit*)

*Visualizes the quantum circuit as a q-sphere*

### Parameters:

`circuit` - the quantum circuit

### Attributes:

`None`

> ## qsphere.`make`(*path: str="qsphere.png"*, *save: bool=True*, *show: bool=True*, *darkmode: bool=True*)

*Returns a Q-Sphere that plots a global visualization of the quantum states in a 3D global view*

### Parameters:

`path (str)` - name of the image to be saved

`save (bool)` - pass True for the graph to be saved

`show (bool)` - pass True for the sphere to be shown instead of saved

`darkmode (bool)` - pass True for darkmode, false for lightmode

### Returns:

`None`

### Example:

```python
from qcpy import quantumcircuit, qsphere

qc = quantumcircuit(3)

qc.h(0)
qc.h(1)
qc.h(2)

sphere_ex = qsphere(qc)
sphere_ex.make(save=False, show=True)
```

> ## *class* qcpy.bloch(*circuit*)

*Visualizes the quantum state of a single qubit as a sphere*

### Parameters:

`circuit` - the quantum circuit

### Attributes:

`None`

> ## blochsphere.`make`(*show_bit: int=0*, *path: str="qsphere.png"*, *save: bool=True*, *show: bool=True*, *darkmode: bool=True*)

*Returns a Bloch Sphere that plots the quantum state of a single qubit in a 3D global view*

### Parameters:

`show_bit (int)` - the qubit on the circuit to be visualized, initialized as the 0th bit

`path (str)` - name of the image to be saved

`save (bool)` - pass True for the graph to be saved

`show (bool)` - pass True for the sphere to be shown instead of saved

`darkmode (bool)` - pass True for darkmode, false for lightmode

### Returns:

`None`

### Example:

```python
from qcpy import quantumcircuit, bloch

qc = quantumcircuit(3)

qc.h(0)
qc.h(1)
qc.h(2)

sphere_ex = bloch(qc)
sphere_ex.make(show_bit=1, save=False, show=True)
```

> ## *class* qcpy.statevector(*circuit*)

*Visualizes the quantum circuit's quantum amplitutes using a bar graph*

### Parameters:

`circuit` - the quantum circuit

### Attributes:

`None`

> ## statevector.`make`(*path: str="statevector.png"*, *save: bool=True*, *show: bool=True*, *darkmode: bool=True*)

*Returns a graph that plots all the amplitudes of the qubits being measured*

### Parameters:

`path (str)` - name of the image to be saved

`save (bool)` - pass True for the graph to be saved

`show (bool)` - pass True for the graph to be shown instead of saved

`darkmode (bool)` - pass True for darkmode and false for lightmode

### Returns:

`None`

### Example:

```python
from qcpy import quantumcircuit, statevector

qc = quantumcircuit(3)

qc.h(0)
qc.h(1)
qc.h(2)

statevector(qc).make(save=False, show=True)
```

> ## *class* qcpy.probability(*circuit*)

*Visualizes the quantum circuit's qubits probability of being measured using a bar graph*

### Parameters:

`circuit` - the quantum circuit

### Attributes:

`None`

> ## probability.`make`(*path: str="probability.png"*, *save: bool=True*, *show: bool=True*, *darkmode: bool=True*)

*Returns a graph that plots all the probabilities of the qubits being measured*

### Parameters:

`path (str)` - name of the image to be saved

`save (bool)` - pass True for the graph to be saved

`show (bool)` - pass True for the graph to be shown instead of saved

`darkmode (bool)` - pass True for darkmode and false for lightmode

### Returns:

`None`

### Example:

```python
from qcpy import quantumcircuit, probability

qc = quantumcircuit(3)

qc.h(0)
qc.h(1)
qc.h(2)

probability(qc).make(save=False, show=True)
```