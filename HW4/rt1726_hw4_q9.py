def permutations(lst, low, high):
	res = []
	if len(lst) == 1:
		return lst
	else:
		for e in lst[low:high + 1]:
			temp_not_e = []
			for j in lst[low: high + 1]:
				if j != e:
					temp_not_e.append(j)
			temp = permutations(temp_not_e, low, high)
			rest = []
			for i in temp:
				rest = [e]
				rest.append(i)
				res.append(flat_list(rest, 0, len(rest) + 1))		
	return res


def flat_list(lst, low, high) :
	fList = []
	if low > high :
		return lst;
	else :
		for e in lst :
			if isinstance(e, list) :
				fList.extend(flat_list(e, 0, len(e)-1));
			else :
				fList.append(e);
	
	return fList

