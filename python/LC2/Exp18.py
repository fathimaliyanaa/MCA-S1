dict1={'a':1,'b':2,'c':3}
dict2={'d':4,'e':5,'f':6}
merged_dict={}
for k,v in dict1.items():
	merged_dict[k]=v
for k,v in dict2.items():
	merged_dict[k]=v
print("Dictionary 1",dict1)
print("Dictionary 2",dict2)
print("merged both dictionary 1&2",merged_dict)
