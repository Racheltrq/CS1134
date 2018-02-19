def find_duplicates(lst):
	count = {}
	for key in range(len(lst)):
		count[key] = 0
	for i in range(len(lst)):
		val = lst[i]
		count[val] += 1
	for key in count:
		if count[key] > 1:
			yield key
