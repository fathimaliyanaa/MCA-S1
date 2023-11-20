list=[ ]
n=int(input("Enter the size:"))
for i in range(0,n):
	a=input("Enter a string:")
	list.append(a)
m=0
for i in list:
	if(m<len(i)):
		m=len(i)
print("Size of the string with longest length:",m)
