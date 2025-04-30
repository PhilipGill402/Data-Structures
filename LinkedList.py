class LinkedList:
    def __init__(self):
        self.front = None
        self.size = 0
    
    def __iter__(self):
        return self.LinkedListIterator(self.front)

    class LinkedListIterator:
        def __init__(self, front):
            self.current = front

        def __iter__(self):
            return self

        def __next__(self):
            if self.current != None:
                val = self.current.value
                self.current = self.current.next
                return val
            else:
                raise StopIteration


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
        
    def add(self, element) -> bool:
        node = self.Node(element)
        if self.isEmpty():
            self.front = node
        else:
            node.next = self.front
            self.front = node

        self.size += 1
        return True

    def remove(self, element) -> bool:
        current = self.front
        prev = None 
        while current != None and current.value != element:
            prev = current 
            current = current.next

        if current == None:
            return False
        elif current == self.front:
            self.front = self.front.next
        else:
            prev.next = current.next

        self.size -= 1 
        return True

    def contains(self, element) -> bool:
        current = self.front

        while current != None:
            if current.value == element:
                return True

            current = current.next

        return False

    def size(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False
    
    def toString(self) -> str:
        string = "["
        current = self.front
        while current != None:
            if current.next != None:
                string += str(current.value) + ", "
            else:
                string += str(current.value)
            current = current.next
        
        string += "]"
        return string