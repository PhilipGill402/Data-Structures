class Stack:
    def __init__(self):
        self.elements = []
        self.top = 0 

    def push(self, value: int):
        self.elements.append(value)
        self.top += 1
        

    def pop(self):
        if not self.isEmpty():
            topValue = self.elements.pop()
            self.top -= 1
            return topValue
        else:
            return -1

    def peek(self):
        if self.isEmpty():
            return None

        return self.elements[self.top]

    def size(self) -> int:
        return self.top
    
    def isEmpty(self) -> bool:
        return self.size() == 0
