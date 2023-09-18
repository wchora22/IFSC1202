n = int(input("Enter N: "))
partialfactorial = 1
for i in range(1, n + 1):
    partialfactorial *= i
print("Sum of factorials: {}".format(partialfactorial))