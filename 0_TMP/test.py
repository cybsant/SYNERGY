class Node:
    def __init__(self):
        self.value = None
        self.left = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, value):
        if self.head.value is None:
            self.head.value = value
            return
        
        temp = Node()
        temp.value = value
        # 1 variant
        # current_node = self.head
        # while current_node.left is not None:
        #     current_node = current_node.left
        # current_node.left = temp
        # 2 variant
        temp.left = self.head
        self.head = temp

    def length(self):
        current_node = self.head
        if current_node.value is None:
            count = 0
        else:
            count = 1
        while current_node.left is not None:
            count += 1
            current_node = current_node.left
        return count
    
    def find_value(self, value):
        if self.head.value is not None:
            if self.head.value == value:
                return True
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.left
        return False

    # def find_node(self, value):
    #     current_node = self.head
    #     while current_node is not None:
    #         if current_node.value == value:
    #             return current_node
    #         current_node = current_node.left
    #     return None
    
    def remove(self, value):
        if self.head.value is not None:
            if self.head.value == value:
                self.head = self.head.left
                return
        current_node = self.head
        while current_node is not None:
            if current_node.left.value == value:
                current_node.left = current_node.left.left
                return
            current_node = current_node.left
    
    def print(self):
        if self.head.value is None:
            print('List is empty')
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.left
        print()


ll = LinkedList()
print(ll.length())
print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(9)
print(ll.length())
print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(7)
print(ll.length())
print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(6)
print(ll.length())
print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(4)
print(ll.length())
print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(9)
print(ll.length())
print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(19)
print(ll.length())
print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(0)
print(ll.length())
print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
ll.print()
#a = 10