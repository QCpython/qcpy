

class DrawSingleGate:
    def __init__(self, gate_icon):
        self.gate = gate_icon

    def __str__(self):
        return self.CreateBox()

    def CreateBox(self):
        inner_width = 3
        vertical_line = u'\u2502'
        horizontal_line = u'\u2500'
        top_left_corner = u'\u250c'
        top_right_corner = u'\u2510'
        bottom_left_corner = u'\u2514'
        bottom_right_corner = u'\u2518'

        top_level =  top_left_corner + (horizontal_line * inner_width) + top_right_corner + "\n"
        middle_region = (vertical_line + ((" " * (inner_width)) + vertical_line + "\n")) * ((inner_width // 2) - 1) \
                        + (vertical_line) + ((" " * (inner_width // 2))) + self.gate + " " + vertical_line + "\n"

        bottom_level = bottom_left_corner + ((horizontal_line * inner_width)) + bottom_right_corner         
        return top_level + middle_region + bottom_level

class DrawSwapGate:
    def __init__(self):
        self.symbol = u'\u2573'

    def __str__(self):
        return self.symbol
