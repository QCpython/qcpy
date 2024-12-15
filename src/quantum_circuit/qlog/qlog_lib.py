import ctypes
import os
from enum import IntEnum

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
QLOG_SO_FILE_PATH = str(FILE_PATH) + "/qlog_engine/qlog_engine.so"
qlog_cross = ctypes.CDLL(QLOG_SO_FILE_PATH)


class qlog_stats_def(ctypes.Structure):
    _fields_ = [("test", ctypes.c_int)]


class qlog_entry_stats_def(ctypes.Structure):
    _fields = []


class qg_entry_gate(IntEnum):
    QLOG_ENTRY_GATE_IDENTITY = 0
    QLOG_ENTRY_GATE_HADAMARD = 1
    QLOG_ENTRY_GATE_PAULIX = 2
    QLOG_ENTRY_GATE_PAULIY = 3
    QLOG_ENTRY_GATE_PAULIZ = 4
    QLOG_ENTRY_GATE_PHASE = 5
    QLOG_ENTRY_GATE_S = 6
    QLOG_ENTRY_GATE_SDG = 7
    QLOG_ENTRY_GATE_T = 8
    QLOG_ENTRY_GATE_TDG = 9
    QLOG_ENTRY_GATE_RZ = 10
    QLOG_ENTRY_GATE_RY = 11
    QLOG_ENTRY_GATE_RX = 12
    QLOG_ENTRY_GATE_SX = 13
    QLOG_ENTRY_GATE_SXDG = 14
    QLOG_ENTRY_GATE_U = 15
    QLOG_ENTRY_GATE_CX = 16
    QLOG_ENTRY_GATE_CH = 17
    QLOG_ENTRY_GATE_CY = 18
    QLOG_ENTRY_GATE_CZ = 19
    QLOG_ENTRY_GATE_CRX = 20
    QLOG_ENTRY_GATE_CRY = 21
    QLOG_ENTRY_GATE_CRZ = 22
    QLOG_ENTRY_GATE_CR1 = 23
    QLOG_ENTRY_GATE_CCX = 24
    QLOG_ENTRY_GATE_QFT = 25
    QLOG_ENTRY_GATE_RCCX = 26
    QLOG_ENTRY_GATE_RC3X = 27
    QLOG_ENTRY_GATE_CUSTOM = 28
    QLOG_ENTRY_GATE_CUSTOMCONTROLLED = 29
    QLOG_ENTRY_GATE_MULTI = 30
    QLOG_ENTRY_GATE_CUSTOMBLOCK = 31
    QLOG_ENTRY_GATE_CUSTOMALGORITHM = 32


class qg_entry_type(IntEnum):
    SINGLE = 0
    CONTROLLED = 1
    MULTI = 2
    BLOCK = 3
    ALGORITHM = 4


class qlog_append_res(IntEnum):
    QLOG_APPEND_SUCCESS = 0
    QLOG_APPEND_FULL = 1
    QLOG_APPEND_ERROR = 2


class qlog_entry_def(ctypes.Structure):
    _fields_ = [
        ("qlog_entry_qubits", ctypes.POINTER(ctypes.c_uint8)),
        ("qlog_entry_qubit_cnt", ctypes.c_uint8),
        ("qlog_entry_gate", ctypes.c_int),
        ("qlog_entry_gate_type", ctypes.c_int),
        ("qlog_entry_stat", qlog_entry_stats_def),
    ]


class qlog_def(ctypes.Structure):
    _fields_ = [
        ("qlog_gate_cnt", ctypes.c_uint16),
        ("qlog_size", ctypes.c_uint16),
        ("qlog_entries", ctypes.POINTER(ctypes.POINTER(qlog_entry_def))),
        ("qlog_stat", qlog_stats_def),
    ]


qlog_cross.qlog_init.argtypes = [ctypes.c_uint8]
qlog_cross.qlog_init.restype = ctypes.POINTER(qlog_def)

qlog_cross.qlog_delete.argtypes = [ctypes.POINTER(qlog_def)]

qlog_cross.qlog_size.argtypes = [ctypes.POINTER(qlog_def)]
qlog_cross.qlog_size.restype = ctypes.c_uint16

qlog_cross.qlog_append.argtypes = [
    ctypes.POINTER(qlog_def),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_uint8,
    ctypes.c_int,
    ctypes.c_int,
]
qlog_cross.qlog_append.restype = qlog_append_res

qlog_cross.qlog_optimize_set.argtypes = [ctypes.POINTER(qlog_def)]
qlog_cross.qlog_optimize_set.restype = ctypes.POINTER(qlog_def)


def convert_qubits_qlog_append(qubits_to_apply):
    return (ctypes.c_uint8 * len(qubits_to_apply))(*qubits_to_apply)
