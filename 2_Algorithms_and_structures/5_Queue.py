from time import sleep

class Queue:
    def __init__(self):
        self.elems = list()

    def add(self, value):
        self.elems.insert(0, value)

    def get(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

queue = Queue()

for i in range(9, -1, -1):
    queue.add(i)
    print(i, end=' ')

print()

for i in range(queue.size()):
    val = queue.get()
    print(val)
    sleep(val)