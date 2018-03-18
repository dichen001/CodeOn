class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.isEmpty():
            self.items.pop()

    def peek(self):
        if (not self.isEmpty()):
            return self.items[-1]