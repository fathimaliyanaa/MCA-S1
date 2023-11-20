limit = int(input("enter the limit:"))
list=[]
for i in range(limit):
	string=input("enter the string:")
	list.append(string)
count=0
for i in list:
	for j in i:
		if j=="a":
			count+=1
print(count) 
