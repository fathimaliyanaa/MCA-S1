list=[ ]
newlist=[ ]
n=int(input("Enter the size:"))
for i in range(0,n):
	el=int(input("Enter element:"))
	list.append(el)
newlist=[x for x in list if x>0]
l=[x*x for x in list]
print(l)
str=input("Enter a string:")
vowels=[i for i in str if i in 'aeiou']
print("list of vowels in string=",vowels)
li=[ord(i) for i in str]
print("ordinal value of given string=",li)
