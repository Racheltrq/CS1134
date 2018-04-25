def find_lst_max(lst):

	if len(lst) == 1:
		return lst[0]

	else:
		res = find_lst_max(lst[1:])
		if res > lst[0]:
			return res
		else:
			return lst[0]

	
lst = [1,7,3,4,5]
print(find_lst_max(lst))