def myfun(n):
	for i in range(1,n+1) :
		if n%3 == 0 and n%5 == 0:
			print(n*myfun(n-1))
		else :
			pass
n = 100
print(myfun(n))
#############################
# def calc_factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * calc_factorial(x-1))

# num = 4
# print("The factorial of", num, "is", calc_factorial(num))