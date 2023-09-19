num = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num==num2 and num2==num3:
    print("3")
elif num==num2 or num2==num3 or num==num3:
    print("2")
else:
    print("0")