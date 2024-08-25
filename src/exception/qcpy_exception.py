class QcpyException:

    def __init__(self, qubits: int, prep: chr):
        self.error = "QCpy error: {}"
        self.qubits = qubits
        self.errorcodes = {
            1: "prepping qubits in quantum circuit using {} is not accepted. \
                Please use x, y, or z for prepping the qubits in the circuit.",
            2: "circuit does not recognize {} as a valid type. Only complex matrices are allowed.",
            3: "array of gates of length {} is out of range of the quantum circuit with {} qubits.",
            4: "{} and {} are out of range of the quantum circuit of size {}.",
            5: "{} is not in range of quantum circuit of size {}.",
        }
        if prep != "z" and prep != "x" and prep != "y":
            raise Exception(self.error.format(self.errorcodes[1].format(prep)))

    def singlegateexcemption(self, qubits_to_apply) -> None:

        if (
            type(qubits_to_apply).__module__ != "complex64"
            and type(qubits_to_apply).__module__ != "complex128"
            and not isinstance(qubits_to_apply, int)
            and not hasattr(qubits_to_apply, "__len__")
        ):
            raise Exception(
                self.error.format(self.errorcodes[2].format(type(qubits_to_apply)))
            )

        elif hasattr(qubits_to_apply, "__len__"):
            if len(qubits_to_apply) > self.qubits:
                raise Exception(
                    self.error.format(
                        self.errorcodes[3].format(len(qubits_to_apply), self.qubits)
                    )
                )

        elif qubits_to_apply >= self.qubits or qubits_to_apply < 0:
            raise Exception(
                self.error.format(
                    self.errorcodes[5].format(qubits_to_apply, self.qubits)
                )
            )

    def multigateexcemption(self, control: int, target: int, gate) -> None:
        if (
            control == target
            or control not in range(self.qubits)
            or target not in range(self.qubits)
        ):
            raise Exception(
                self.error.format(
                    self.errorcodes[4].format(control, target, self.qubits)
                )
            )

    # def customgatequeueexception(self, queue) -> None:
    #     pass
