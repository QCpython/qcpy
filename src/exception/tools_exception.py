class ToolsException:

    def __init__(self):
        pass

    def test_probability(self, show_percent: bool, show_bit, round: int, size: int):
        pass

    def test_measure(self, state):
        pass

    def test_amplitude(self, show_bit, round: int, amplitude, size: int) -> None:

        if round <= 0:
            exit(1)

        if (not isinstance(show_bit, int) and show_bit > 0) or (
            not isinstance(show_bit, str) or not isinstance(show_bit, int)
        ):
            exit(1)

    def test_phase_angle(self, show_bit, round: int, radian: bool):
        pass
