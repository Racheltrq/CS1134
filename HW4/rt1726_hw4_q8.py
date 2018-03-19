
def flat_list(lst, low, high):
	fList = []
	if low > high:
		return lst
	else :
		for e in lst:
			if isinstance(e, list):
				fList.extend(flat_list(e, 0, len(e)-1))
			else:
				fList.append(e)
	
	return fList

