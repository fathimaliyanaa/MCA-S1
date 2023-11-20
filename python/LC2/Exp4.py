x=[]
n=int(input("enter the number of elements in x:"))
for i in range(0,n):
	a=int(input("Enter the elements:"))
	if(a<=100):
		x.append(a)
	else:
		x.append("over")
print(x)
