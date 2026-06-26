#Ask the user to enter the lengths of all three sides of a triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))   
side3 = float(input("Enter the length of the third side: "))

#Calculate the area of the triangle.
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

#Print the area
print(f"The area of the triangle is: {area}")