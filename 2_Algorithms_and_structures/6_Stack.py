from time import sleep

class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)
        #self.items.insert(0, item)

    def pop(self):
        val = self.items.pop()
        #val = self.items.pop(0)
        return val

    def size(self):
        return len(self.items)

stack = Stack()

for i in range(10):
    stack.push(i)
    print(i, end=' ')

print()

for i in range(stack.size()):
    val = stack.pop()
    print(val)
    sleep(val)