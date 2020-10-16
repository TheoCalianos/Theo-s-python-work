from LinkedListT import *

myList = LinkedListList(1)
myList.addToFront(2.3)
myList.addToFront(10000.123)
myList.addToFront(-123)

print(myList.getByIndex(2).getValue())
myList.addAtIndex(212, 2)
print(myList.getByIndex(2).getValue())
