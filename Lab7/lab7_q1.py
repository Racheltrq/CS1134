def get_tag(expr):
	expr = expr.strip()
	n = len(expr)
	i = 0
	left_index = 0
	right_index = 0

	while i < n and found == False:
		if expr[i] != '<':
			i += 1
		else:
			left_index = i
			while expr[i] != '>':
				i += 1
			right_index = i
			break
	yield '<' + expr[left_index : right_index + 1] + '>'


