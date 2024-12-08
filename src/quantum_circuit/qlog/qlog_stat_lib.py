import ctypes


class qlog_stats_def(ctypes.Structure):
    _fields_ = [("test", ctypes.c_int)]


class qlog_entry_stats_def(ctypes.Structure):
    _fields_ = []
