class Queue:
    def __init__(self, capacity: int = 10):
        self.front = None 
        self.rear = None 
        self.numElements = 0
    
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
        
        def len(self) -> int:
            length = 1 
            current = self.next
            while current != None:
                length += 1
                current = current.next
            
            return current

    def enqueue(self, element):
        node = self.Node(element)
        if self.isEmpty():
            self.rear = node
            self.front = self.rear
        else:
            self.rear.next = node
            self.rear = node

        self.numElements += 1
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            value = self.front.value
            self.front = self.front.next
            if self.size() == 1:
                self.rear = self.front
            
            self.numElements -= 1
            return value
    
    def first(self):
        if self.isEmpty():
            return None
        else:
            return self.front.value
        
    def size(self) -> int:
        return self.numElements
    
    def isEmpty(self) -> bool:
        return self.size() == 0
    