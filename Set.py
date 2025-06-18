from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')

class Set(Generic[T]):
    def __init__(self):
        self.__size = 0
        self.__index = 0
        self.__elements: list[T] = []

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index == len(self.__elements):
            raise StopIteration
        val = self.__elements[self.__index]
        self.__index += 1
        return val

    def __len__(self):
        return self.__size

    def __str__(self):
        string = "("
        for i in range(len(self.__elements)):
            val = str(self.__elements[i])
            if i == len(self.__elements) - 1:
                string += val
            else:
                string += val + ", "
        string += ")"
        return string

    def add(self, element: T) -> int:
        newElements = self.__elements.copy() + [None]
        #find insertion point
        idx = 0
        for i in range(len(self.__elements)):
            val = self.__elements[i]
            if element < val:
                idx = i
                break

            #element is in the set already
            elif element == val:
                return -1
        else:
            idx = len(self.__elements)
        
        #shift from insertion point
        for i in range(len(self.__elements) - 1, idx - 1, -1):
            newElements[i+1] = self.__elements[i]

        #insert value
        newElements[idx] = element

        #adds in the rest of the values
        for i in range(idx):
            newElements[i] = self.__elements[i]

        #copy newElements to elements
        self.__elements = newElements.copy()
        self.__size += 1
        return 1

    def remove(self, element: T) -> int:
        #find element
        for i in range(len(self.__elements)):
            if self.__elements[i] == element:
                idx = i
                break
        else:
            return -1

        #remove element
        self.__elements[i] = None
        
        #shift values
        for i in range(idx + 1, len(self.__elements)):
            self.__elements[i- 1] = self.__elements[i]

        #remove last value as it is a duplicate or None
        self.__elements = self.__elements[:len(self.__elements)-1]

        #decrements the size variable
        self.__size -= 1

        return 1

    def contains(self, element: T, left=0, right=None) -> int:
        if right is None:
            right = len(self.__elements)
        middle = (left + right) // 2

        #not found
        if left >= right:
            return -1

        #we found it
        if element == self.__elements[middle]:
            return middle
        #its on the left half
        elif element < self.__elements[middle]:
            return self.contains(element, left, middle)
        #its on the right half
        else:
            return self.contains(element, middle+1, right)

    def intersection(self, other: Set) -> Set:
        newSet = Set()
        selfItr = iter(self)
        otherItr = iter(other)
        selfVal = next(selfItr)
        otherVal = next(otherItr)
        selfIdx = 1
        otherIdx = 1
        print(len(self))
        while selfIdx <= len(self) and otherIdx <= len(other):
            if selfVal == otherVal:
                newSet.add(selfVal)
                try:
                    selfVal = next(selfItr)
                    otherVal = next(otherItr)
                    selfIdx += 1
                    otherIdx += 1
                except StopIteration:
                    break
            elif selfVal < otherVal:
                try:
                    selfVal = next(selfItr)
                    selfIdx += 1
                except StopIteration:
                    break
            else:
                try:
                    otherVal = next(otherItr)
                    otherIdx += 1
                except StopIteration:
                    break

        return newSet

    def union(self, other: Set) -> Set:
        newSet = Set()

        for i in self:
            newSet.add(i)

        for i in other:
            newSet.add(i)
            

        return newSet

    def difference(self, other: Set) -> Set:
        newSet = Set()

        for i in self:
            if other.contains(i) == -1:
                newSet.add(i)

        return newSet

    def isEmpty(self):
        return self.size() == 0
