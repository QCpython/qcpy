from .qlog_lib import qlog_cross


class QLog:
    def __init__(self, qubits: int):
        self.qubits = qubits
        self.qlog = qlog_cross.qlog_init(qubits)
