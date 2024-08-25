from scipy import sparse as sp
from ...quantum_gate import identity
from ..interface import SingleGateInterface


class SparseSingleGate(SingleGateInterface):
    def __init__(self, qubits: int, big_endian: bool = False):
        self.qubits = qubits
        self.big_endian = big_endian
        return

    def __create_gate_queue__(self, qubits_to_apply, gate):
        sparse_identity = sp.csr_matrix(identity())
        gate_queue = [sparse_identity] * self.qubits
        if type(qubits_to_apply) == int:
            gate_queue[qubits_to_apply] = gate
        elif hasattr(qubits_to_apply, "__len__"):
            for i in qubits_to_apply:
                if i >= self.qubits:
                    print("Error: qubit is out of range")
                    exit(1)
                else:
                    gate_queue[i] = gate
        else:
            print("Error: invalid paramater type: 'qubits_to_apply'.")
            exit(1)
        if self.big_endian:
            gate_queue = gate_queue[::-1]
        return gate_queue