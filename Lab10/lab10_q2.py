class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"

class boost_queue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        self.data.size()

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, elem):
        self.data.add_last(elem)

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.data.delete_last()

    def first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.data.first_node().data

    def boost(self, k):
        if (self.is_empty()):
            raise Exception("List is empty")
        temp = self.data.delete_last()
        k = k % self.data.size
        cursor = self.data.last_node().prev
        i = 1
        while i != k:
            cursor = cursor.prev
            i += 1
        self.data.add_after(cursor, temp)

a = boost_queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.enqueue(6)
print(a.data)
print(a.first())
print(a.dequeue())
a.boost(2)
print(a.data)