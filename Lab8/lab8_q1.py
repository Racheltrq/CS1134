class Empty(Exception):
    pass
    
class ArrayDeque:
	INITIAL_CAPACITY = 10

	def __init__(self):
		self.data = [None] * ArrayDeque.INITIAL_CAPACITY
		self.front_ind = 0
		self.num_of_elems = 0

	def __len__(self):
		return self.num_of_elems

	def is_empty(self):
		return (len(self) == 0)

	def first(self):
		if self.is_empty:
			raise Empty('The queue is empty')
		else:
			return self.data[self.front_ind]

	def last(self):
		if self.is_empty:
			raise Empty('The queue is empty')
		else:
			return self.data[(self.front_ind + self.num_of_elems - 1) % len(self.data)]

	def add_first(self, elem):
		if self.num_of_elems == len(self.data):
			self.resize(2 * len(self.data))
		first = (self.front_ind - 1) % len(self.data)
		self.data[first] = elem
		self.front_ind = first
		self.num_of_elems += 1

	def add_last(self, elem):
		if self.num_of_elems == len(self.data):
			self.resize(2 * len(len.data))
		self.data[(self.front_ind + self.num_of_elems) % len(self.data)] = elem
		self.num_of_elems += 1

	def delete_first(self):
		if self.is_empty == True:
			raise Empty('The queue is empty')
		res = self.data[self.front_ind]
		self.data[self.front_ind] == None
		self.front_ind = (self.front_ind + 1) % len(self.data)
		self.num_of_elems -= 1
		if self.num_of_elems < len(self.data) // 4:
			self.resize(len(self.data) // 2)
		return res

	def delete_last(self):
		if self.is_empty == True:
			raise Empty('The queue is empty')
		back = (self.front_ind + self.num_of_elems) % len(self.data)
		res = self.data[back]
		self.data[back] = None
		self.num_of_elems -= 1
		if self.num_of_elems < len(self.data) // 4:
			self.resize(len(self.data) // 2)
		return res

	def resize(self, capacity):
		temp = self.data
		self.data = [None] * capacity
		temp_ind = self.front_ind
		for new_ind in range(self.num_of_elems):
			self.data[new_ind] = temp[temp_ind]
			temp_ind = (temp_ind + 1) % len(temp)
		self.front_ind = 0

a = ArrayDeque()
a.add_first(1)
a.add_first(2)
a.add_last(3)
print(a.data)
a.delete_first()
a.delete_last()
print(a.data)