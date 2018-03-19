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


def postfix_calc():
	input_str = input('-->')
	arr = ArrayStack()
	dic = {}
	while input_str != 'done()':

		temp = ''
		for i in input_str:
			if i != ' ':
				temp += i
		input_str = temp

		assign = ''
		if '=' in input_str:
			index = input_str.find('=')
			assign = input_str[:index]
			input_str = input_str[index + 1:]


		for i in input_str:
			
			if i not in '+-*/':
				if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
					arr.push(dic[i])
				else:	
					arr.push(int(i))
			else:
				temp2 = arr.pop()
				temp1 = arr.pop()
				if i == '+':
					arr.push(temp1 + temp2)
				elif i == '-':
					arr.push(temp1 - temp2)
				elif i == '*':
					arr.push(temp1 * temp2)
				else:
					if temp2 == 0:
						raise ZeroDivisionError("division by zero")
					else:
						arr.push(temp1 / temp2)

		res = arr.pop()
		if assign != '':
			dic[assign] = res

		print(res)
		input_str = input('-->')

postfix_calc()