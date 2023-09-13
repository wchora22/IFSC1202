firstprevious = 1
secondprevious = 0
finnumber= int(input("Enter Fibonacci sequence number: "))
for i in range(2, finnumber+1):
    currentvalue = firstprevious+secondprevious
    secondprevious = firstprevious
    firstprevious = currentvalue
print(currentvalue)