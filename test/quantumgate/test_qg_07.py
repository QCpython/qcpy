import numpy as np

from qcpy.quantumgate import swap


def test_qg_07():
    assert (
        swap()
        == np.array(
            [
                [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
                [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
                [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
                [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
            ],
            "F",
        )
    ).all(), "test_qg_07 Failed on Swap"
