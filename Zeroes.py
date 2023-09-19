n = int(input("Enter N: "))
count = 0
num = 0
for i in range(n):
    num = int(input("Enter the number: "))
    if num == 0:
        count+=1
print("Number of zeroes: {}".format(count))