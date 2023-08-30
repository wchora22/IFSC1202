side1 = float(input("Enter side1: "))
side2 = float(input("Enter side2: "))
side3 = float(input("Enter side3: "))
g = (side1+side2+side3)/2
area = (g*(g-side1)*(g-side2)*(g-side3))**0.5
print("The area of a triangle is: ", area)