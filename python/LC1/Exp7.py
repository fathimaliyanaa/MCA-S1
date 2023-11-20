string=input("enter a string")
n=int(input("enter number of copies:"))
if n<0:
	print("please enter a non negative integer")
else:
	result=string*n
print(result)
