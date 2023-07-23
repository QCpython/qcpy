# """
# QMACE Testing - 08

# """

# from QCpy import QuantumCircuit
# from QCpy.Core import qmace

# def inc(x):
#     qc = QuantumCircuit(qubits = x, prep = 'z')
#     qc.swap(0, x - 1)
#     return qc.state()

# def inc_2(x):
#     qc = qmace.QuantumCircuit(qubits = x, prep = 'z')
#     qc.swap(0, x - 1)
#     return qc.execute().state()


# def test_28a():
#     assert (inc(2) == inc_2(2)).all(), "test_28a Failed"

# def test_28b():
#     assert (inc(3) == inc_2(3)).all(), "test_28b Failed"

# def test_28c():
#     assert (inc(4) == inc_2(4)).all(), "test_28c Failed"

# def test_28d():
#     assert (inc(5) == inc_2(5)).all(),"test_28d Failed"

