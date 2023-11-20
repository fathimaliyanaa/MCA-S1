list=input("Enter the colors comma seperated:")
color=list.split(',')
if color:
	first_color=color[0]
	last_color=color[-1]
print("First color:",first_color)
print("Last color:",last_color)
