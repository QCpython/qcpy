class DrawSingleGate:
    def __init__(self, gate_icon):
        self.symbol = gate_icon
    def __str__(self):
        return self.symbol
    
class DrawSwapGate:
    def __init__(self):
        self.symbol = u'\u2573'
    def __str__(self):
        return self.symbol
    
class EmptySegment:
    def __init__(self):
        self.symbol = u'\u2500'
    def __str__(self):
        return self.symbol
    def __eq__(self, other):
        return self.symbol == other.symbol
