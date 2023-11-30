def add_integers(*args):
	"""
	Adds variable_length integer arguments.
	parameters:
		*args(int):variable_length integer arguments.
	Returns:
		int sum of the integer arguments.
	"""
	return sum(args)
input_numbers=input("Enter integers seperated by spaces:").split()
input_numbers=[int(num)for num in input_numbers]
result=add_integers(*input_numbers)
print("The sum of the integer is:",result)
