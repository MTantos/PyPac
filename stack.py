class Stack(object):
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        return None
