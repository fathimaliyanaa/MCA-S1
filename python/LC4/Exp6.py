square_area=lambda side:side**2
rectangle_area=lambda length,width:length*width
triangle_area=lambda base,height:0.5*base*height

side_length=float(input("Enter the length of a side of a square:"))
rectangle_length=float(input("Enter the length of a rectangle:"))
rectangle_width=float(input("Enter the width of a rectangle:"))
triangle_base=float(input("Enter the base of a triangle:"))
triangle_height=float(input("Enter the height of a triangle:"))

print("Area of square:",square_area(side_length))
print("Area of rectangle:",rectangle_area(rectangle_length,rectangle_width))
print("Area of triangle:",triangle_area(triangle_base,triangle_height))
