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

