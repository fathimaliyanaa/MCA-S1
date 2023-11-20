list=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
	num=int(input(f"Enter element {i+1}:"))
	list.append(num)
sum_of_items=0
for item in list:
	sum_of_items+=item
print("The sum of all items in the list is:",sum_of_items)
