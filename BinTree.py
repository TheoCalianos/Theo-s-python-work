from BiTreeNode import *


class BinTree:
    baseNode = None
    size = 0
    root = BiTreeNode

    def addRecursive(self, value, currentNode=None):

        if currentNode is None:
            self.root = BiTreeNode(value)
            return
        if value < currentNode.getValue():
            self.addRecursive(value, currentNode.getLeft())
        elif value > currentNode.getValue:
            self.addRecursive(value, currentNode.getRight())
        else:
            return currentNode
        return currentNode

    def Add(self, value):
        self.root = self.addRecursive(value, self.root)
        self.size += 1

    def containsNodeRecursive(self, currentNode, value):
        if currentNode is None:
            return False
        if value == currentNode.getValue():
            return True
        if value < currentNode.getValue():
            self.containsNodeRecursive(currentNode.getLeft(), value)
        else:
            self.containsNodeRecursive(currentNode.getRight(), value)

    def containsNode(self, value):
        return self.containsNodeRecursive(self.root, value)

    def deleteNodeRecursive(self, currentNode, value, pointer):
        if currentNode is None:
            return None
        if value == currentNode.getValue:
            return 0
            # privous Node?
            # get greater value of the deleted none if was a right of the dleted node
            # get less than if the deleted nod was a left of its previous node
        if value < currentNode.getValue():
            self.deleteNodeRecursive(currentNode.getLeft(), value, "Left")
        else:
            self.deleteNodeRecursive(currentNode.getRight(), value, "Right")
