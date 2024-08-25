class Wire:
    def __init__(self):
        self.length = 0
        self.content = []

    def add(self, to_add: str) -> None:
        self.length += 1
        self.content.append(to_add)

    def insert(self, to_insert: int, to_add: str) -> None:
        if to_insert >= self.length:
            self.add(to_add)
        else:
            self.content[to_insert] = to_add

    def at(self, index: int) -> str:
        return "" if index >= self.length else self.content[index]
