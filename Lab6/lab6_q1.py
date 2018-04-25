def powers_of_two(n):
	count = 0
	while count < n:
		yield 2 ** (count + 1)
		count += 1

for curr_value in powers_of_two(6):
	print(curr_value)