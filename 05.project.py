startrange = int(input("Enter the start of range: "))
endofrange = int(input("Enter the end of range: "))
for r in range(startrange,endofrange+1):
    n = r
    length=0
    while n > 0:
        n//=10
        length=length + 1
    n=r
    sum=0
    while n > 0:
        digit=n%10
        sum=sum+digit**length
        n//=10
    if sum == r:
        print(r)