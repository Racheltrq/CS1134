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

def merge_linked_lists(srt_lnkl_lst1, srt_lnkl_lst2):
    res = DoublyLinkedList()
    return merge_sublists(srt_lnkl_lst1, srt_lnkl_lst2, srt_lnkl_lst1.header.next, srt_lnkl_lst2.header.next, res)

def merge_sublists(srt_lnkl_lst1, srt_lnkl_lst2, cursor1, cursor2, res):
    if cursor1 is srt_lnkl_lst1.trailer:
        while cursor2 is not srt_lnkl_lst2.trailer:
            res.add_last(cursor2.data)
            cursor2 = cursor2.next
        
    elif cursor2 is srt_lnkl_lst2.trailer:
        while cursor1 is not srt_lnkl_lst1.trailer:
            res.add_last(cursor1.data)
            cursor1 = cursor1.next

    else:

        if cursor1.data > cursor2.data:
            res.add_last(cursor2.data)
            cursor2 = cursor2.next
        else:
            res.add_last(cursor1.data)
            cursor1 = cursor1.next
        merge_sublists(srt_lnkl_lst1, srt_lnkl_lst2, cursor1, cursor2, res)
    return res

'''
srt_lnkl_lst1 = DoublyLinkedList()
srt_lnkl_lst2 = DoublyLinkedList()

srt_lnkl_lst1.add_last(1)
srt_lnkl_lst1.add_last(3)
srt_lnkl_lst1.add_last(5)
srt_lnkl_lst1.add_last(6)
srt_lnkl_lst1.add_last(8)

print(merge_linked_lists(srt_lnkl_lst1, srt_lnkl_lst2))
'''