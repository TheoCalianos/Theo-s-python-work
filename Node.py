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
