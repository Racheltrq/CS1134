def sort_first(lst):
	if len(lst) == 0:
		return
	else:
		sort_first_helper(lst, 0, 1)


def sort_first_helper(lst, pivot, index):
	if index == len(lst):
		return
	else:
		if lst[index] < lst[pivot]:
			temp = lst.pop(index)
			lst.insert(0, temp)
			pivot += 1

		sort_first_helper(lst, pivot, index + 1)
		

lst = [12, 1, 4, 33, 6, 2, 10]
sort_first(lst)
print(lst)