def print_triangle(n):
	if n == 1:
		print ('*')
	else:
		print_triangle(n - 1)
		print(n * '*')


def print_oposite_triangles(n):
	if n > 1:
		print('*' * n);
		print_oposite_triangles(n - 1);
		print('*' * n);
	else:
		print('*\n*')

def print_ruler(n):
	 if n == 2:
	 	print('-')
	 	print('-' * n)
	 	print('-')



	 else:
	 	print_ruler(n - 1)
	 	print('-' * n)
	 	print_ruler(n - 1)


