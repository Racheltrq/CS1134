

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

	def __str__(self):
		s = ''
		for item in self.data:
			s += str(item) + ' '
		return s


def convert_infix_exp_to_postfix(infix_exp_str):
	arr_par = ArrayStack()
	arr_op = ArrayStack()
	arr_res = ArrayStack()
	index = 0
	while index < len(infix_exp_str):
		if infix_exp_str[index] == '(':
			arr_par.push('(')
		elif infix_exp_str[index] == ')':
			arr_par.pop()
			op = arr_op.pop()
			arr_res.push(op)
		elif ord('0') <= ord(infix_exp_str[index]) <= ord('9'):
			arr_res.push(infix_exp_str[index])

		elif infix_exp_str[index] in '+-*/':
			arr_op.push(infix_exp_str[index])
		index += 1
	return str(arr_res)

print(convert_infix_exp_to_postfix('(2 + ((3 * 4)-5))'))
