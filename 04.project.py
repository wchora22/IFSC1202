startrange= int(input("Enter the start of the range: "))
endrange= int (input("Enter the end of the range: "))
for n in range (startrange, endrange):
    for i in range (2,n//2+1):
        if n%i== 0: 
            break
    else:
        print("Prime", n)
