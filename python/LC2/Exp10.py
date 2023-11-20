color_list1=input("enter the first list:").split(" ")
color_list2=input("enter the second list:").split(" ")
color_list=[item for item in color_list1]
color_list2=[item for item in color_list2]
result=[item for item in color_list1 if item not in color_list2]
print("values from color_list1 not contained in color_list2:",result)
