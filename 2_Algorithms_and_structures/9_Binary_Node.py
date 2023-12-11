from platform import node


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = Node()

    def add(self, value):
        if self.root.value is None:
            self.root.value = value
            return
        self.add_data(self.root, value)

    def add_data(self, current, value):
        if current.value > value:
            if current.left is None:
                current.left = Node()
                current.left.value = value
                current.left.parent = current
            else:
                self.add_data(current.left, value)
        else:
            if current.right is None:
                current.right = Node()
                current.right.value = value
                current.right.parent = current
            else:
                self.add_data(current.right, value)

    def find(self, value):
        if self.root.value is None:
            return False
        if self.root.value == value:
            return True
        node = self.find_node(self.root, value)
        if node is None:
            return False
        return True

    def find_node(self, current, value):
        if current is None:
            return None
        if current.value == value:
            return True
        if current.value > value:
            return self.find_node(current.left, value)
        else:
            return self.find_node(current.right, value)

    def find_min(self):
        node = self.find_min_node(self.root)
        return node.value

    def find_min_node(self, current):
        if current.left is None:
            return current
        return self.find_min_node(current.left)

    def find_max(self):
        node = self.find_max_node(self.root)
        return node.value

    def find_max_node(self, current):
        if current.right is None:
            return current
        return self.find_max_node(current.right)

    def _delete(self, value):
            if self.root.left is None and self.root.right is None and self.root.value == value:
                self.root.value = None
                return

            if self.root.left is not None and self.root.right is None and self.root.value == value:
                self.root = self.root.left
                self.root.parent = None
                return

            if self.root.left is None and self.root.right is not None and self.root.value == value:
                self.root = self.root.right
                self.root.parent = None
                return



bst = BinarySearchTree()
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(10)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(8)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(9)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(7)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(20)
print(bst.find(10), bst.find(8), bst.find(20))

print(bst.find_min(), bst.find_max())

#a = 10

bst = BinarySearchTree()
bst.add(10)
bst.add(8)
bst._delete(10)

a = 10