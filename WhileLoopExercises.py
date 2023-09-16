n =0
n2=0
n3=0
count=0
while n != 0:
    n = int(input("Enter a number (CR to quit): "))
        if n != 0:
        n2=n
    if n>n2:
        n3 += 1
        n3 = 1
        n2 = n
print ("Number of values greater than the previous: ", count)