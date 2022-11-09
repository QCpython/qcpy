from QuantumCircuit import QuantumCircuit
import numpy as np

def inc(x):
    qc = QuantumCircuit(qubits = x, little_endian = True, prep = 'z')
    qc.hadamard(0)
    qc.hadamard(1)
    qc.hadamard(2)
    qc.hadamard(3)
    qc.hadamard(4)
    qc.hadamard(5)
    qc.rxx(0,1)
    qc.rxx(2,3)
    qc.rxx(4,5)
    qc.rx(5)
    return qc.state()

def test_16a():
    print(inc(6))
    assert (inc(6) == np.array([ -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j, -0.125+0j ]).reshape(64, 1)).all(), "test_16a Failed"

test_16a()