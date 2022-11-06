# README.md

# QCpy - A Quantum Computing Library for Python

QCpy is an open source python library and collaborative project for flexible simulations and visualizations of quantum circuits. Designed by college students with students in mind, this library contains a powerful set of tools to teach computer scientists about the emerging discipline of quantum computing (QC).

## Recommended Resources on Quantum Computing:

- [Microsoft’s Linear Algebra for Quantum Computing](https://learn.microsoft.com/en-us/azure/quantum/overview-algebra-for-quantum-computing)
- [IBM’s Quantum Computing: a field guide](https://quantum-computing.ibm.com/composer/docs/iqx/guide/)
- [Wikipedia: Quantum Computing](https://en.wikipedia.org/wiki/Quantum_computing)

---

# Qubits

> ## *class* QC.Qubit.Qubit(*initial_state=’z’*)

*Object representation of a qubit.*

### Parameters:

`initial_state (chr)` - Character input for starting direction in the *x*, *y*, or *z* axis.

### Attributes:

`state (numpy.ndarray)` -  current state of qubit in matrix representation.

---

# Quantum Gates

> ## *class* QC.QuantumGate.Identity()

*Gate that does not modify the quantum state.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Identity gate.

```python
Identity.matrix = [1+0j, 0+0j], 
	                [0+0j, 1+0j]
```

> ## *class* QC.QuantumGate.PauliX()

*Quantum equivalent of the NOT gate in classical computing with respect to the standard basis |0>, |1>.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Pauli-X gate.

```python
PauliX.matrix = [0+0j, 1+0j], 
	              [1+0j, 0+0j]
```

> ## *class* QC.QuantumGate.PauliY()

*Rotation around y-axis of the bloch sphere by π radiains, mapping |0> to i|1> and |1> to -i|0>.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Pauli-Y gate.

```python
PauliY.matrix = [0+0j, 0-1j],
                [0+1j, 0+0j]
```

> ## *class* QC.QuantumGate.PauliZ()

*Rotation around z-axis of the bloch sphere by π radiains, mapping |1> to -|1>; known as the phase-flip.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Pauli-Z gate.

```python
PauliY.matrix = [1+0j, 0+0j], 
                [0+0j, -1+0j]
```

> ## *class* QC.QuantumGate.Hadamard()

*Maps the basis states |0> to |+> and |1> to |->, creating a superposition state if given a computation basis state.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of Hadamard gate.

```python
Hadamard.matrix = ([1,  1] 
                   [1, -1]) * (1/sqrt(2))
```

> ## *class* QC.QuantumGate.CNot(*inverse=False*)

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

> ## *class* QC.QuantumGate.Swap()

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

> ## *class* QC.QuantumGate.Toffoli()

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

> ## *class* QC.QuantumGate.Phase(*theta=numpy.pi/2*)

*Applies a rotation of theta around the z-axis.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around z-axis.

### Attributes:

`matrix (np.ndarray)` - matrix representation of Phase gate.

```python
Phase.matrix = [1+0j, 0+0j],
			         [0+0j, numpy.exp(0+1j * theta)]
```

> ## *class* QC.QuantumGate.S()

*Equivalent to a pi/2 rotation around the z-axis.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of S gate.

```python
S.matrix = [1+0j, 0+0j],
           [0+0j, 0+1j]
```

> ## *class* QC.QuantumGate.Sdg()

*Inverse of S gate; a -pi/2 rotation around the z-axis.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of an inverse S gate.

```python
Sdg.matrix = [1+0j, 0+0j],
             [0+0j, 0-1j]
```

> ## *class* QC.QuantumGate.T()

*Square of S gate; where T = S^2.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of a T gate.

```python
T.matrix = [1+0j, 0+0j],
           [0+0j, numpy.exp((0+1j * numpy.pi) / 4)]
```

> ## *class* QC.QuantumGate.Tdg()

*Inverse of T gate.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of a inverse of T gate.

```python
Tdg.matrix = [1+0j, 0+0j],
             [0+0j, numpy.exp((0-1j * numpy.pi) / 4)]
```

> ## *class* QC.QuantumGate.Rz(*theta=numpy.pi/2*)

*Rotation of qubit around the z-axis.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around z-axis.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Rz gate.

```python
Rz.matrix = [numpy.exp((0-1j * (theta / 2))), 0+0j],
            [0+0j, numpy.exp(0+1j * (theta / 2))]
```

> ## *class* QC.QuantumGate.Rx(*theta=numpy.pi/2*)

*Rotation of qubit around the x-axis.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around x-axis.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Rx gate.

```python
Rx.matrix = [numpy.cos(theta / 2), 0-1j * numpy.sin(theta / 2)],
            [0-1j * numpy.sin(theta / 2), numpy.cos(theta / 2)]
```

> ## *class* QC.QuantumGate.Ry(*theta=numpy.pi/2*)

*Rotation of qubit around the y-axis.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around y-axis.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Ry gate.

```python
Ry.matrix = [numpy.cos(theta / 2), -1 * numpy.sin(theta / 2)],
            [numpy.sin(theta / 2), numpy.cos(theta / 2)]
```

> ## *class* QC.QuantumGate.Sx()

*Rotation around the x-axis by 90 degrees in the counter-clockwise direction. Also known as the “square-root X gate” due to the fact that applying the SX gate twice results in an X gate.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Sx gate.

```python
Sx.matrix = [1+1j, 1-1j], 
            [1-1j, 1+1j]]) * (1 / 2)
```

> ## *class* QC.QuantumGate.Sxdg()

*Inverse of the Sx gate.*

### Parameters:

`None`

### Attributes:

`matrix (np.ndarray)` - matrix representation of an inverse Sx gate.

```python
Sxdg.matrix = [1-1j, 1+1j], 
              [1+1j, 1-1j]]) * (1 / 2)
```

> ## *class* QC.QuantumGate.U(*theta=numpy.pi/2, phi=numpy.pi/2, lmbda=numpy.pi/2*)

*Rotation of qubit with respect to theta, phi, and lambda, in Euler angles.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around Euler angle theta.

`phi (float)`default: `numpy.pi/2` -  angle of rotation around Euler angle phi.

`lmbda (float)`default: `numpy.pi/2` -  angle of rotation around Eulear angle lambda.

### Attributes:

`matrix (np.ndarray)` - matrix representation of a U gate.

```python
U.matrix = [numpy.cos(theta / 2), -1 * numpy.exp(0+1j * lmbda) * numpy.sin(theta / 2)], 
           [numpy.exp(0+1j * phi) * numpy.sin(theta / 2), numpy.exp(0+1j * (lmbda + phi)) * numpy.cos(theta / 2)]]
```

> ## *class* QC.QuantumGate.Rxx(*theta=numpy.pi/2*)

*Rotation about XX, maximally entangling at theta = pi/2.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around XX.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Rxx gate.

```python
Rxx.matrix = [numpy.cos(theta / 2), 0+0j, 0+0j, 0-1j * numpy.sin(theta / 2)],
             [0+0j, numpy.cos(theta / 2), 0-1j * numpy.sin(theta / 2), 0+0j],
             [0+0j, 0-1j * numpy.sin(theta / 2), numpy.cos(theta / 2), 0+0j],
             [0-1j * numpy.sin(theta / 2), 0+0j, 0+0j, numpy.cos(theta / 2)]
```

> ## *class* QC.QuantumGate.Rzz(*theta=numpy.pi/2*)

*Rotation about ZZ, maximally entangling at theta = pi/2.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation around ZZ.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Rzz gate.

```python
Rzz.matrix = [numpy.exp(0-1j * (theta / 2)), 0+0j, 0+0j, 0+0j],
             [0+0j, numpy.exp(0+1j * (theta / 2)), 0+0j, 0+0j],
             [0+0j, 0+0j, numpy.exp(0+1j * (theta / 2)), 0+0j],
             [0+0j, 0+0j, 0+0j, numpy.exp(0-1j * (theta / 2))]
```

> ## *class* QC.QuantumGate.Cr(*theta=numpy.pi/2*)

*Controlled phase shift rotation in theta radians; generalization of Cz gate.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation in theta radians.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Cr gate.

```python
Cz.matrix = [1+0j, 0+0j, 0+0j, 0+0j],
            [0+0j, 1+0j, 0+0j, 0+0j],
            [0+0j, 0+0j, 1+0j, 0+0j],
            [0+0j, 0+0j, 0+0j, numpy.exp(theta * 0+1j)]
```

> ## *class* QC.QuantumGate.Cz(*theta=numpy.pi/2*)

*Controlled phase shift rotation in theta radians.*

### Parameters:

`theta (float)`default: `numpy.pi/2` -  angle of rotation in theta radians.

### Attributes:

`matrix (np.ndarray)` - matrix representation of an Cz gate.

```python
Cz.matrix = [1+0j, 0+0j, 0+0j, 0+0j],
            [0+0j, 1+0j, 0+0j, 0+0j],
            [0+0j, 0+0j, 1+0j, 0+0j],
            [0+0j, 0+0j, 0+0j, -1+0j]
```
---