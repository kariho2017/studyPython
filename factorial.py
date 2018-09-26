def factorial(x):
	if x == 0:
		return 1
	else:
		return x * factorial(x - 1)


for i in range(10):
	print("hello")