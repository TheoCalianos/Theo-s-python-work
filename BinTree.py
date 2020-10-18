from BiTreeNode import *


class BinTree:
    baseNode = None
    size = 0

    def addLeaf(self, value, currentNode=None):
        nextNode = None
        if currentNode is not None:
            if value < currentNode.getValue():
                if currentNode.hasLeft():
                    nextNode = currentNode.getLeft()
                    self.addLeaf(nextNode)
                else:
                    currentNode.setLeft(BiTreeNode(value))
            elif value > currentNode.getValue:
                if currentNode.hasRight():
                    nextNode = currentNode.getRight()
                    self.addLeaf(nextNode)
                else:
                    currentNode.setRight(BiTreeNode(value))
        else:
            self.addLeaf(self.baseNode)
