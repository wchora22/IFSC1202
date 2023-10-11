values= input("Enter values seperated by Space: ")
lst= values.split(" ")
for i in range(len(lst)):
    if int(lst[i])%2==1:
        print(lst[i])