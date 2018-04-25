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



class CompactString: 
	def __init__(self, orig_str = None):

		self.data = DoublyLinkedList()
		index = 0
		if orig_str != None:
			while index < len(orig_str):
				count = 1
				while (index + count) < len(orig_str) and orig_str[index + count] == orig_str[index + count - 1]:

					count += 1
				add = (orig_str[index], count)
				self.data.add_last(add)
				index += count


	def __add__(self, other):
		res = CompactString()
		cursor = self.data.header.next
		while cursor is not self.data.trailer:
			res.data.add_last(cursor.data)
			cursor = cursor.next
		cursor = other.data.header.next
		while cursor is not other.data.trailer:
			res.data.add_last(cursor.data)
			cursor = cursor.next
		return res

	def __lt__(self, other):
		if self.data.is_empty() is True:
			return True
		if other.data.is_empty() is True:
			return False
		cursor1 = self.data.header.next
		cursor2 = other.data.header.next
		left = cursor1.data[1] - cursor2.data[1]
		while cursor1 is not self.data.trailer and cursor2 is not self.data.trailer:
			if cursor1.data[0] > cursor2.data[0]:
				return False
			elif cursor1.data[0] < cursor2.data[0]:
				return True


			if left < 0:

				cursor1 = cursor1.next
				if cursor1.data is not None:
					left += cursor1.data[1]
				else:
					return True
			elif left > 0:
				cursor2 = cursor2.next
				if cursor2.data is not None:
					left += cursor2.data[1]
				else:
					return False
			else:
				cursor1 = cursor1.next
				cursor2 = cursor2.next
				left = cursor1.data[1] - cursor2.data[1]
		return False

	def __le__(self, other):
		if self.data.is_empty() is True:
			return True
		if other.data.is_empty() is True:
			return False
		cursor1 = self.data.header.next
		cursor2 = other.data.header.next
		left = cursor1.data[1] - cursor2.data[1]
		while cursor1 is not self.data.trailer and cursor2 is not self.data.trailer:
			if cursor1.data[0] > cursor2.data[0]:
				return False
			elif cursor1.data[0] < cursor2.data[0]:
				return True


			if left < 0:

				cursor1 = cursor1.next
				if cursor1.data is not None:
					left += cursor1.data[1]
				else:
					return True
			elif left > 0:
				cursor2 = cursor2.next
				if cursor2.data is not None:
					left += cursor2.data[1]
				else:
					return False
			else:
				cursor1 = cursor1.next
				cursor2 = cursor2.next
				left = cursor1.data[1] - cursor2.data[1]
		return True

	def __gt__(self, other):
		if self.data.is_empty() is True:
			return False
		if other.data.is_empty() is True:
			return True
		cursor1 = self.data.header.next
		cursor2 = other.data.header.next
		left = cursor1.data[1] - cursor2.data[1]
		while cursor1 is not self.data.trailer and cursor2 is not self.data.trailer:
			if cursor1.data[0] > cursor2.data[0]:
				return True
			elif cursor1.data[0] < cursor2.data[0]:
				return False


			if left < 0:

				cursor1 = cursor1.next
				if cursor1.data is not None:
					left += cursor1.data[1]
				else:
					return False
			elif left > 0:
				cursor2 = cursor2.next
				if cursor2.data is not None:
					left += cursor2.data[1]
				else:
					return True
			else:
				cursor1 = cursor1.next
				cursor2 = cursor2.next
				left = cursor1.data[1] - cursor2.data[1]
		return False

	def __ge__(self, other):
		if self.data.is_empty() is True:
			return False
		if other.data.is_empty() is True:
			return True
		cursor1 = self.data.header.next
		cursor2 = other.data.header.next
		left = cursor1.data[1] - cursor2.data[1]
		while cursor1 is not self.data.trailer and cursor2 is not self.data.trailer:
			if cursor1.data[0] > cursor2.data[0]:
				return True
			elif cursor1.data[0] < cursor2.data[0]:
				return False


			if left < 0:

				cursor1 = cursor1.next
				if cursor1.data is not None:
					left += cursor1.data[1]
				else:
					return False
			elif left > 0:
				cursor2 = cursor2.next
				if cursor2.data is not None:
					left += cursor2.data[1]
				else:
					return True
			else:
				cursor1 = cursor1.next
				cursor2 = cursor2.next
				left = cursor1.data[1] - cursor2.data[1]
		return True

	def __repr__(self):
		return ''.join([i[0] * i[1] for i in self.data])

'''
def debug():
	a = CompactString('aaa')
	b = CompactString('')
	print(a > b)

debug()
'''