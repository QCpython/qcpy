def multi_control(is_connector: bool = False, is_end: bool = False) -> str:
    res = "     ──■──  │  "
    if is_connector:
        res = "  │  ──■──  │  "
    elif is_end:
        res = "  │  ──■──     "
    return res


def multi_connect() -> str:
    return "  │  ──┼──  │  "


def horizontal_line() -> str:
    return "     ─────     "


def block_bottom() -> str:
    return "│   │┤   ├└───┘"


def block_connect():
    return "│   │┤   ├│   │"


def block_gate(gate: str) -> str:
    return "│   │┤MUL├│   │"


def block_top() -> str:
    return "┌───┐┤   ├│   │"


def single_gate(gate, is_controlled: bool = False, is_start: bool = False):
    top = "┌─┴─┐" if (is_controlled and not is_start) else "┌───┐"
    middle = "┤"
    if len(gate) == 1:
        middle += " " + gate + " ├"
    elif len(gate) == 2:
        middle += gate + " ├"
    else:
        middle += gate + "├"
    return top + middle + ("└───┘" if not is_start else "└─┬─┘")


def swap_point():
    return "     ──╳──     "


def vertical_line():
    return "       │       "
