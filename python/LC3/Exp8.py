n=int(input("Enter a number:"))
reverse=0
temp=n
while temp>0:
	digit=temp%10
	reverse=reverse*10+digit
	temp=temp//10
print("Reverse of the number:",reverse) 
