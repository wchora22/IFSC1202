x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
if x > 0 and y > 0:
    # x is greater than 0, y is greater than 0
    print("Quadrant I")
elif x > 0 and y < 0:    
    print("Quadrant IV")
elif y > 0:    
    print("Quadrant II")
else:
    print("Quadrant III")
