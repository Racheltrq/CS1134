import ArrayStack
def eval_postfix_exp(boolean_exp_str):
	lst = boolean_exp_str.split(' ')
	arr = ArrayStack.ArrayStack()

	for i in lst:
		arr.push(i)

	res1 = True
	res2 = True
	and_or = arr.pop()
	
	operator = arr.pop()
	num2 = arr.pop()
	num1 = arr.pop()
	if operator == '>':
		res1 = num1 > num2
	elif operator == '<':
		res1 = num1 < num2
	elif operator == '=':
		res1 = (num1 == num2)
	else:
		return 'Error'

	operator = arr.pop()
	num2 = arr.pop()
	num1 = arr.pop()
	if operator == '>':
		res1 = num1 > num2
	elif operator == '<':
		res1 = num1 < num2
	elif operator == '=':
		res1 = (num1 == num2)
	else:
		return 'Error'


	if and_or == '&':
		return res1 and res2
	else:
		return res1 or res2

	


print(eval_postfix_exp('1 2 < 6 3 < &'))
