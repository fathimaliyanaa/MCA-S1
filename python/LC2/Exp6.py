list1=[]
list2=[]
li=int(input("enter length of list 1:"))
for i in range(0,li):
	x=int(input("enter the elements:"))
	list1.append(x)
l2=int(input("enter the length of list2:"))
for i in  range(0,l2):
	x=int(input("enter the element:"))
	list2.append(x)
if len(list1)==len(list2):
	print("list1 & list2 have same length")
else:
	print("list1 & list2 have different length")
if sum(list1)==sum(list2):
	print("sum of list1 & list2 are same")
else:
	print("sum of list1 & list2 are different")
x=set(list1).intersection(list2)
if x:
	print("common elements are",x)
else:
	print("there is no common elements")

