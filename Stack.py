class Stack:
    def __init__(self):
        self.elements = []
        self.top = None

    def push(self, value: int):
        self.top += 1
        self.elements[self.top] = value

    def pop(self):
        self.elements.pop()
        self.top -= 1

    def peek(self):
        if self.isEmpty():
            return None

        return self.elements[self.top]

    def size(self) -> int:
        return self.top
    
    def isEmpty(self) -> bool:
        return self.size() == 0
