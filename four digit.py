num = int(input("Enter a number: "))
m=num
rev=0
while num>0:
    r=num%10
    rev = rev *10 +r
    num = num // 10
if rev == m:
    print("Yes")
else:
    print("No")