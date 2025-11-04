def circle_area(radius):
    area= 3.14159*(radius)**2
    return area;

radius = float(input("Enter the radius"))
final = circle_area(radius)
print("The area of the circle with radius", radius, "is", final)