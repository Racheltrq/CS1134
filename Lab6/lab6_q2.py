def find_sum(lst):
	if lst == []:
		return 0
	else:
		if type(lst) == int:
			return lst

	return find_sum(lst[0]) + find_sum(lst[1:])

lst = [[1, 2], [3, [[4], 5]], 6]
print(find_sum(lst))