class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.add_data(self.root, value)

    def add_data(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = BinaryNode(value)
            else:
                self.add_data(current.left, value)
        else:
            if current.right is None:
                current.right = BinaryNode(value)
            else:
                self.add_data(current.right, value)

    def find(self, value):
        return self.find_node(self.root, value) is not None

    def find_node(self, current, value):
        if current is None or current.value == value:
            return current
        if value < current.value:
            return self.find_node(current.left, value)
        else:
            return self.find_node(current.right, value)

    def find_min(self):
        current = self.find_min_node(self.root)
        return current.value
        
    def find_min_node(self, current):
        while current.left is not None:
            current = current.left
        return current
    
    def find_max(self):
        current = self.find_max_node(self.root)
        return current.value

    def find_max_node(self, current):
        while current.right is not None:
            current = current.right
        return current
    

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

a = 10
