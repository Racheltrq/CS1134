class ArrayStack:
	def __init__(self):
		self.data = []


	def __len__(self):
		return len(self.data)

	def is_empty(self):
		if len(self) == 0:
			return True
		else:
			return False

	def push(self, elem):
		self.data.append(elem)

	def pop(self):
		if self.is_empty == True:
			raise Exception('Stack is empty')

		return self.data.pop()

	def top(self):
		if self.is_empty == True:
			raise Exception('Stack is empty')
		return self.data[-1]

