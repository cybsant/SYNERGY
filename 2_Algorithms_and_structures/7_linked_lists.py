class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, value):
        if self.head.value is None:
            self.head.value = value
            return
        temp = Node()
        temp.value = value
        temp.next = self.head
        self.head = temp

    def length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def find_value(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    """ ДЗ № 7.1 [ удаление элемента из односвязного списка ] """
    def delete_value(self, value): 
        if self.head.value == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    """ ДЗ № 7.2 [ вставка элемента после какого-то элемента ] """
    def insert_after(self, value, new_value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                new_node = Node()
                new_node.value = new_value
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    """ ДЗ № 7.3 [ перевернуть список в обратном направлении ] """
    def reverse_list(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    """ ДЗ № 7.4 [ отсортировать список ] """
    def sort_list(self):
        swapped = True
        while swapped:
            swapped = False
            current_node = self.head
            while current_node.next is not None:
                if current_node.value > current_node.next.value:
                    current_node.value, current_node.next.value = current_node.next.value, current_node.value
                    swapped = True
                current_node = current_node.next

    def print_list(self):
        if self.head.value is None:
            print('List is empty')
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next
        print()
    
ll = LinkedList()

""" ДЗ № 7 [ тест функций ] """
ll.add(9)
ll.add(7)
ll.add(6)
ll.add(4)
ll.add(9)
ll.add(19)
ll.add(0)
print('- Initial list')
ll.print_list()  # Output: 0 19 9 4 6 7 9

ll.delete_value(4)
print('- Delete 4')
ll.print_list()  # Output: 0 19 9 6 7 9

ll.insert_after(0, 10)
print('- Insert 10 after 0')
ll.print_list()  # Output: 0 10 19 9 6 7 9

ll.reverse_list()
print('- Reversed list')
ll.print_list()  # Output: 9 7 6 9 19 10 0

ll.sort_list()
print('- Sorted list')
ll.print_list()  # Output: 0 6 7 9 9 10 19

# print(ll.length())
# print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
# ll.print_list()
# ll.add(9)
# print(ll.length())
# print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
# ll.print_list()
# ll.add(7)
# print(ll.length())
# print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
# ll.print_list()
# ll.add(6)
# print(ll.length())
# print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
# ll.print_list()
# ll.add(4)
# print(ll.length())
# print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
# ll.print_list()
# ll.add(9)
# print(ll.length())
# print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
# ll.print_list()
# ll.add(19)
# print(ll.length())
# print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
# ll.print_list()
# ll.add(0)
# print(ll.length())
# print(ll.find_value(0), ll.find_value(9),ll.find_value(6))
# ll.print_list()
