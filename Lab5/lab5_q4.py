def binary_serch(srt_lst, val , low, high):
	if low == high:
		return 'None'

	else:
		mid = (low + high) // 2
		if srt_lst[mid] < val:
			return binary_serch(srt_lst, val, mid, high)
		if srt_lst[mid] > val:
			return binary_serch(srt_lst, val, low, mid)
		else:
			return mid


lst = [1,2,3,4,5,6,7]
print(binary_serch(lst, 4, 0, 5))
