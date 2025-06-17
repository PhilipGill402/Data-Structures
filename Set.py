class Set:
    def __init__(self):
        self.size = 0
        self.index = 0
        self.elements = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.elements[self.index]

    def add(self, element):
        newElements = self.elements.copy() + [None]
        #find insertion point
        idx = 0
        for i in range(len(self.elements)):
            val = self.elements[i]
            if element < val:
                idx = i
                break

            #element is in the set already
            elif element == val:
                return -1
        else:
            idx = len(self.elements)
        
        #shift from insertion point
        for i in range(len(self.elements) - 1, idx - 1, -1):
            newElements[i+1] = self.elements[i]

        #insert value
        newElements[idx] = element

        #adds in the rest of the values
        for i in range(idx):
            newElements[i] = self.elements[i]

        #copy newElements to elements
        self.elements = newElements.copy()
        self.size += 1
        self.index += 1
        return 1

    def contains(self, element, left=0, right=None):
        if right is None:
            right = len(self.elements)
        middle = (left + right) // 2

        #not found
        if left >= right:
            return -1

        #we found it
        if element == self.elements[middle]:
            return middle
        #its on the left half
        elif element < middle:
            return self.contains(element, left, middle)
        #its on the right half
        else:
            return self.contains(element, middle+1, right)

    def size(self):
        return self.size()

    def isEmpty(self):
        return self.size() == 0

if __name__ == "__main__":
    newSet = Set()

    for i in range(10):
        newSet.add(i)
