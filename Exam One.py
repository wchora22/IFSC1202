startofrange= int(input("Enter start of range: "))
endofrange= int (input ("Enter end of range: "))
print("Special numbers between {}".format(startofrange), "and {}".format(endofrange))
for r in range(startofrange,endofrange+1):
    num=r
    length=0
    while num >0:
        num//=10
        length=length+1
    num=r
    sum=0
    while num>0:
        dig=num%10
        num//=10
        prod=1
        for h in range(1, dig+1):      
            prod = prod*dig
        sum=sum+prod
    if sum == r:
        print (r)