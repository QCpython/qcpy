

class DrawSingleGate:
    def __init__(self, gate_icon):
        self.gate = gate_icon
        self.draw_gate = ""

    def __str__(self):
        return self.CreateBox()

    def CreateBox(self):
        inner_width = 5
        final_box = ""

        vertical_line = u'\u2502'
        horizontal_line = u'\u2500'
        top_left_corner = u'\u250c'
        top_right_corner = u'\u2510'
        bottom_left_corner = u'\u2514'
        bottom_right_corner = u'\u2518'
        final_box += top_left_corner + (horizontal_line * inner_width) + top_right_corner + "\n" + ((vertical_line + (" " * inner_width) + \
                                        vertical_line + "\n") * ((inner_width // 2))) + bottom_left_corner + ((horizontal_line * inner_width)) + bottom_right_corner
        return final_box
