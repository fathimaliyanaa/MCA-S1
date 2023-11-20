dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
sorted_dict_ascending=[]
for k,v in dict1.items():
	sorted_dict_ascending.append((v,k))
	sorted_dict_ascending.sort()
	sorted_dict_descending=[]
for k,v in dict1.items():
	sorted_dict_descending.append((v,k))
	sorted_dict_descending.sort(reverse=True)
print("Dictionary in ascending order:")
print(sorted_dict_ascending)
print("Dictionary in descending order:")
print(sorted_dict_descending)
