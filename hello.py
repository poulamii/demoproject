def factorial(x):
	if x==0:
		return 1
	else:
		return x*factorial(x-1)
number=s
result=factorial(number)
print(f"the factorial of {number} is {result}")
