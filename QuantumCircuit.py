"""
QuantumCircuit.py
"""
from Qubit import Qubit

class QuantumCircuit:
    def __init__(self, bit_str: str):
        self._bit_str = bit_str # string of qubits bits in system
        self._qubit_array = [] # array holding qubits
        # 
    def x(self, bit: int):
        """
        X-Gate Operation on specified qubit.
        Params:
            bit (int): the nth-bit position on circuit.
        Returns:
            None
        """
        pass
    def y(self):
        pass
    def z(self):
        pass
    def hadamard(self):
        pass
    def t(self):
        pass
    def swap(self):
        pass
    def cnot(self):
        pass
    def measure(self):
        pass
    def probalities(self):
        pass
    def graph(self):
        pass