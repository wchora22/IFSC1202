values= input("Enter values seperated by spaces: ")
lst=values.split(' ')
for i in range(0,len(lst)):
    if i<len(lst)-1:
        if int(lst[i+1])>int(lst[i]):
            print(int(lst[i+1]))