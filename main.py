class Node:
    __value = None
    __next = None

    def __init__(self, _value, node=None):
        self.__value = _value
        self.__next = node

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value
        return self.__value

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next
        return self.__next

    def hasNext(self):
        return self.getNext() is not None


class IntList(Node):
    __head = None
    __value = None
    size = 0

    def __init__(self, value):
        _value = value
        self.__head = Node(value)
        self.size += 1

    def addToFront(self, num):
        self.__head = Node(num, self.__head)
        return self.__head

    def printList(self):
        currentNode = self.__head
        while currentNode.hasNext():
            print(currentNode.getValue())
            currentNode = currentNode.getNext()
        print(currentNode.getValue())


myList = IntList(2)
myList.addToFront(5.6)
myList.addToFront(8)
myList.addToFront(6)
myList.printList()
