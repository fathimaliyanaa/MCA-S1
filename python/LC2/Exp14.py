str=input("Enter the string:")
str1=str[-3]+str[-2]+str[-1]
if(str1=="ing"):
	str=str+"ly"
else:
	str=str+"ing"
print(str)
