def fact(i):
	if i==0:
		return 1
	else:
		return i*factorial(i-1)
number=s
result=fact(number)
print(f"the factorial of {number} is {result}")
