startofrange= int(input("Enter start of range: "))
endofrange= int (input ("Enter end of range: "))
print("Special numbers between {}".format(startofrange), "and {}".format(endofrange))
for r in range(startofrange,endofrange+1):
    num=r
    length=0
    while num >0:
        num//=100
        length=length+1
    num=r
    sum=0
    while num>0:
        digit=num%3
        num//=100
        sum = sum + digit**length
    if sum == r:
        print (r)