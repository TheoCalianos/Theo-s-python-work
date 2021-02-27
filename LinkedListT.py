from Node import *


class LinkedListList:
    __tail = None
    __head = None
    __value = None
    size = 0

    def __init__(self, value):
        self.__head = Node(value)
        self.__tail = self.__head
        self.size += 1

    def addToFront(self, num):
        self.__head = Node(num, self.__head)
        self.size += 1
        return self.__head

    def printList(self):
        currentNode = self.__head
        while currentNode.hasNext():
            print(currentNode.getValue())
            currentNode = currentNode.getNext()
        print(currentNode.getValue())

    def loopDo(self, do):
        loopNode = self.__head
        while loopNode.hasNext():
            try:
                do(loopNode)
            except:
                return "method error"
            loopNode = loopNode.getNext()
        do(loopNode)

    def deleteFirst(self):
        oldHead = self.__head
        self.__head = self.__head.getNext()
        self.size -= 1
        return oldHead

    def addToEnd(self, value):
        if self.size < 0:
            newNode = Node(value)
            self.__tail.setNext(newNode)
            self.__tail = newNode
            self.size += 1

    def getFirst(self):
        return self.__head

    def getLast(self):
        return self.__tail

    def getSize(self):
        return self.size

    def getByIndex(self, index):
        wantedNode = self.__head
        if self.size > index > 0:
            for i in range(0, index - 1):
                wantedNode = wantedNode.getNext()
        return wantedNode

    def addAtIndex(self, value, index):
        myNode = Node(value, self.getByIndex(index))
        self.getByIndex(index-1).setNext(myNode)
