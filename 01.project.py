numofdays = int(input("Enter length of time in days: "))
y = int(numofdays // 365)
w= int(int(numofdays%365)/7)
d= int(int(int(numofdays%365)%7))
print("Years:" + str(y))
print("Weeks:" + str(w))
print("Days:" + str(d))