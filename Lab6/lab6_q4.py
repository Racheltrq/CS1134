import ctypes


#def make_str(n):
    #return n * ctypes.py_object


class MyString(initial_str = ''):
	def __init__(self, initial_str):
		self.s = initial_str


	def len(self):
		return self.s.__len__()

	def iter(self):
		for i in range(len(self)):
			return self[i]

	def repr(self):
		return self

	def get_item(self, n):
		if n < len(self):
			return self[n]
		else:
			raise IndexError('invalid index')

	def add(self, other):
		return self.s + other.s

	def radd(self, other):
		return other.s + self.s

	def upper(self):
		return self.upper()


a = MyString('abc')
print(len(a))



        
