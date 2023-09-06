num1= float(input("Enter first number: "))

operator=(input("Enter operator (+,-,*,/): "))
num2 = float(input("Enter second number: "))
if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "*":
    result = num1*num2
    print(result)
elif operator == "/":
    result = num1/num2
    print(result)
else:
    print("Invalid operator")