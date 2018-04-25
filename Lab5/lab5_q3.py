def is_palindrome(input_str, low, high):
	if low == high:
		return True
	if low == high - 1:
		if input_str[low] == input_str[high]:
			return True
		else:
			return False

	else:
		res = is_palindrome(input_str, low + 1, high - 1)
		if input_str[low] == input_str[high]:
			return res and True
		else:
			return res and False

print(is_palindrome('12321', 0, 4))