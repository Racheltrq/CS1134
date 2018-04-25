import os
def disk_usage(path):
	size = 0
	if os.path.isdir(path):
		return os.path.getsize(path)

	
	else:
		lst = os.listdir(path)
		for i in lst:
			path_file = os.path.join(path, i)
			size += disk_usage(path_file)
	return size


print(disk_usage("D:/Project1"))