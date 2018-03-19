

def count_lowercase(s, low, high, c=0):
	if low > high:
		return c
	else:
		if s[low].islower():
			c += 1
		return count_lowercase(s, low+1, high, c); 




def is_number_of_lowercase_even(s, low, high, c = 0):
	if low > high:
		return c
	else:
		if s[low].islower():
			c += 1
		return count_lowercase(s, low+1, high, c) % 2 == 0

