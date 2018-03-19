def list_min(lst, low, high):
	if low == high:
		return lst[0]
	else:
		temp = lst[0]
		for i in range(low + 1, high + 1):
			if lst[i] < temp:
				temp = lst[i]
		list_min(lst, low + 1, high)
		return temp

