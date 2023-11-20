l=[ ]
n=int(input("Enter the length of the list:"))
for i in range(0,n):
	x=int(input("Enter the integers:"))
	l.append(x)
print(l)
for i in l:
	if(i%2==0):
		l.remove(i)
print(l)
