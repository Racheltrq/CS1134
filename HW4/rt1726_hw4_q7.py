def split_by_sign(lst, low, high):
	if low > high:
		return
	else:
		if lst[low] < 0:
			temp = lst.pop(low)
			lst.insert(0, temp)
		if lst[low] == 0:
			index = low - 1
			found = False
			while index >= 0:
				if lst[index] < 0:
					lst.pop(low)
					lst.insert(index + 1, 0)
					found = True
					break
				index -= 1
			if found == False:
				lst.pop(low)
				lst.insert(0, 0)


		split_by_sign(lst, low + 1, high)


lst = [3, 4, -5, 1, -9, -2, 4, 1, 0, -1, -3]
split_by_sign(lst, 0, 10)
print(lst)