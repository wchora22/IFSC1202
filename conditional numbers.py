num= int(input("Enter first number: "))
num2 = int (input("Enter the second number: "))
num3 = int (input("Enter the third number: "))
smallest=num
if(num2 <num) and (num2<num3):
    smallest = num2
elif (num3 < num):
    smallest = num3
print (smallest)