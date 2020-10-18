class BiTreeNode:
    value = None
    right = None
    left = None

    def __init__(self, _value, _right=None, _left=None):
        self.value = _value
        self.right = _right
        self.left = _left

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.value = value
        return self.value

    def getRight(self):
        return self.right

    def setRight(self, _right):
        self.right = _right
        return self.right

    def hasRight(self):
        return self.getRight() is not None

    def getLeft(self):
        return self.left

    def setLeft(self, _left):
        self.left = _left
        return self.left

    def hasLeft(self):
        return self.getLeft() is not None
