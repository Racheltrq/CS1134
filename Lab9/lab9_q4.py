class Empty(Exception):
    pass

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
          raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Empty("List is empty")
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
            raise Empty("List is empty")
        return self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("List is empty")
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

def reverse_list_change_elements_order(lnk_lst):
    if (lnk_lst.is_empty()):
        return
    cursor1 = lnk_lst.first_node()
    cursor2 = lnk_lst.last_node()
    while cursor1 != cursor2 and cursor1 != cursor2.next:
        temp = cursor1.data
        cursor1.data = cursor2.data
        cursor2.data = temp
        cursor1 = cursor1.next
        cursor2 = cursor2.prev

def reverse_list_change_nodes_order(lnk_lst):
    if (lnk_lst.is_empty()):
        return
    firstNode = lnk_lst.header.next
    cursor = firstNode
    lnk_lst.header.next = lnk_lst.trailer.prev
    while cursor.data is not None:
        cursor.next, cursor.prev = cursor.prev, cursor.next
        cursor = cursor.prev
    firstNode.next = cursor
    cursor.prev = firstNode


a = DoublyLinkedList()
a.add_last(1)
a.add_last(2)
a.add_last(3)
a.add_last(4)
a.add_last(5)
a.add_last(6)
a.add_last(7)
print(a)
reverse_list_change_nodes_order(a)
print(a)


