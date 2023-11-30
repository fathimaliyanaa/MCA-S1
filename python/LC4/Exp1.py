def simple_interest(p,t,r):
	simpleinterest=(p*t*r)/100
	print("simple interest =",simpleinterest)
p=float(input("Enter principal amount:"))
t=float(input("Enter the time period(in years):"))
age=int(input("Enter your age:"))
if(age<60):
	simple_interest(p,t,r=10)
else:
	simple_interest(p,t,r=12)
