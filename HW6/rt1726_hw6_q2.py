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


class Integer:
	def __init__(self, num_str = None):
		self.data = DoublyLinkedList()
		if num_str != None:
			index = 0
			while index != len(num_str) and num_str[index] == '0':
				index += 1
			if index == len(num_str):
				index -= 1
			for i in num_str[index:]:
				self.data.add_last(int(i))


	def __add__(self, other):
		s1 = len(self.data)
		s2 = len(other.data)

		
		res = Integer()
		num1 = None
		num2 = None
		if s2 > s1:
			num1 = self.data
			num2 = other.data
		else:
			num1 = other.data
			num2 = self.data
		for i in range(abs(s1-s2)):
			num1.add_first(0)
		cursor1 = num1.trailer.prev
		cursor2 = num2.trailer.prev
		add = 0
		while cursor1 is not num1.header:
			temp = int(cursor1.data + cursor2.data + add)
			add = 0
			if temp > 9:
				add = 1
				temp -= 10
			res.data.add_first(temp)
			cursor1 = cursor1.prev
			cursor2 = cursor2.prev
		if add == 1:
			res.data.add_first(1)

		return res

	def __mul__(self, other):
		print('mul:', self, other)
		res = Integer()
		other_num = 0
		cursor = other.data.trailer.prev

		cursor1 = self.data.trailer.prev
		for i in range(len(self.data)):
			for j in range(cursor1.data * (10 ** i)):
				res +=  other
			cursor1 = cursor1.prev
		if res.data.header.next.data == None:
			return 0
		return res


	def __repr__(self):
		res = ''
		for i in self.data:
			res += str(i)
		return res

'''
n1 = Integer('00000000')
n2 = Integer('3')
print(n1)
print(n2)

n3 = n1 * n2
print(n3)
'''
