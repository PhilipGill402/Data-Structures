from LinkedList import *
from Stack import *
from Queue import *

arr = Queue() 

for i in range(10):
    arr.enqueue(i)

for i in range(5):
    print(arr.dequeue())

print("\n")
print(arr.first())