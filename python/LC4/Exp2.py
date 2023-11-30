def even_or_odd(number):
	if number%2==0:
		return"Even"
	else:
		return"Odd"
n=int(input("Enter a number:"))
result=even_or_odd(n)
print(f"The number is",result)
