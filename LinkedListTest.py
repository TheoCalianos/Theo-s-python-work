from LinkedListT import *
def test_AddToFront():
    MyLinkedList = LinkedListList(1)
    print(MyLinkedList.getByIndex(0).getValue())
    MyLinkedList.addToFront(10)
    MyLinkedList.addToFront(-10)
    MyLinkedList.addToFront(324234.212)
    MyLinkedList.addToFront(.123)
    print(MyLinkedList.getByIndex(0).getValue())
    print(MyLinkedList.getByIndex(1).getValue())
    print(MyLinkedList.getByIndex(2).getValue())
    print(MyLinkedList.getByIndex(3).getValue())
    print(MyLinkedList.getByIndex(4).getValue())
    print(MyLinkedList.getByIndex(5).getValue())

test_AddToFront()