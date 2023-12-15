from graphics.rectangle import *
from graphics.circle import area as circleArea, perimeter as circumference
from graphics.threeDgraphics.cuboid import *
from graphics.threeDgraphics.sphere import surface_area as sphereTSA, volume as sphereVolume

l=int(input("Enter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
rect_area = area(l, b)
rect_perimeter = perimeter(l, b)
print(f"Rectangle Area: {rect_area}")
print(f"Rectangle Perimeter: {rect_perimeter}")

r=int(input("Enter the radius of the circle : "))
circle_area = circleArea(r)
circle_perimeter = circumference(r)
print(f"Circle Area: {circle_area}")
print(f"Circle Perimeter: {circle_perimeter}")

length=int(input("Enter the length of cuboid : "))
width=int(input("Enter the width of cuboid : "))
height=int(input("Enter the height of cuboid : "))
cuboid_area = surface_area(length, width, height)
cuboid_volume = volume(length, width, height)
print(f"Cuboid Surface Area: {cuboid_area}")
print(f"Cuboid Volume: {cuboid_volume}")

radius=int(input("Enter the radius of the sphere : "))
sphere_area = sphereTSA(radius)
sphere_volume = sphereVolume(radius)
print(f"Sphere Surface Area: {sphere_area}")
print(f"Sphere Volume: {sphere_volume}")
