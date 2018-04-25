def product_evens(lst, n):

	if len(lst) == 1:
		if lst[0] % 2 == 0:
			return lst[0]
		else:
			return 1
	else:
		res = product_evens(lst[1:], n)
		if lst[0] % 2 == 0 and lst[0] <= n:
			return res * lst[0]
		else:
			return res


lst = [1,2,3,4,5,100,12,2]
print(product_evens(lst, len(lst)))