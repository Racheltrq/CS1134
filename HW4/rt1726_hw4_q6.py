def appearances(s, low, high):
	if low > high:
		return {}
	else:
		dic = {}
		return appearances_helper(s, low, high, dic)

def appearances_helper(s, low, high, dic):
	if low > high:
		return
	else:
		if s[low] not in dic:
			dic[s[low]] = 1
		else:
			dic[s[low]] += 1
		print(dic)
		appearances_helper(s, low + 1, high, dic)
		return dic
