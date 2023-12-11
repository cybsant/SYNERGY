
class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [Node() for _ in range(size)]
        
    def _hash(self, key):
        return key % len(self.buckets)

    def add(self, value):
        hash = self._hash(value)
        if self.buckets[hash].data is None:
            self.buckets[hash].data = value
        else:
            current = self.buckets[hash]
            while current.next is not None:
                current = current.next
            current.next = Node()
            current.next.data = value

    def _delete(self, value):
        hash = self._hash(value)
        if self.buckets[hash].data is None:
            raise ValueError("Value not found")
        else:
            prev = None
            current = self.buckets[hash]
            if current.data == value:
                if prev is None:
                    self.buckets[hash] = current.next
                else:
                    prev.next = current.next
                return
            while current.next is not None:
                prev = current
                current = current.next
                if current.data == value:
                    prev.next = current.next
            raise ValueError("Value not found")

    def find(self, value):
        hash = self._hash(value)
        current = self.buckets[hash]
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False


ht = HashTable(10)
ht.add(3)
ht.add(13)
ht.add(23)

try:
    ht._delete(3)
    ht._delete(13)
    ht._delete(23)
except ValueError as e:
    print(str(e))

a = 10