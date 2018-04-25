class Empty(Exception):
    pass

class boost_queue:
	def __init__(self):
		self.data = [None] * 4
		self.front_ind = 0
		self.num_of_elems = 0

	def __len__(self):
		return self.num_of_elems

	def is_empty(self):
		return self.num_of_elems == 0

	def enqueue(self, elem):
		if len(self.data) == self.num_of_elems:
			self.resize(2 * len(self.data))
		back = (self.front_ind + self.num_of_elems) % len(self.data)
		self.data[back] = elem
		self.num_of_elems += 1

	def dequeue(self):
		if self.is_empty == True:
			raise Empty(Exception)
		res = self.data[self.front_ind]
		self.data[self.front_ind] = None
		self.front_ind = (self.front_ind + 1) % len(self.data)
		self.num_of_elems -= 1
		if self.num_of_elems < len(self.data) // 4:
			self.resize(len(self.data) // 2)
		return res

	def first(self):
		if self.is_empty == True:
			raise Empty(Exception)
		return self.data[self.front_ind]

	def resize(self, capacity):
		temp = self.data
		self.data = [None] * capacity
		temp_ind = self.front_ind
		for new_ind in range(self.num_of_elems):
			self.data[new_ind] = temp[temp_ind]
			temp_ind = (temp_ind + 1) % len(temp)
		self.front_ind = 0


def find_sum(lst):
	res = 0
	queue = boost_queue()
	for i in lst:
		queue.enqueue(i)
	while queue.is_empty() == False:
		temp = queue.dequeue()
		if type(temp) == list:
			for j in temp:
				queue.enqueue(j)
		else:
			res += temp
	print(res)


lst = [[1, 2], [3, [[4], 5]], 6]
find_sum(lst)