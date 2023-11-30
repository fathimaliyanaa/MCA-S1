def compare(s1,s2,n):
	return s1[:n]==s2[:n]
string1=input("Enter the first string:")
string2=input("Enter the second string:")
n=int(input("Enter the value of n:"))
result=compare(string1,string2,n)
print(f"The first {n} character of both strings are {'equal' if result else 'not equal'}")
