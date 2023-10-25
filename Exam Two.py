a = []
numberfile = open("Exam Two Properties.csv", 'r')
x = numberfile.readline().strip()
y = x.split(", ")
a.append(y)
x = numberfile.readline().strip()
while x != "":
    y = x.split(",")
    a.append(y)
    x = numberfile.readline().strip()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end='')
    print()
zipcodes = []
rowzip=-1
columnzip=-1
properties=
price=float()
for i in range(len(properties)):
    if properties[0][i]==zipcodes:
        rowzip=i
for i in range(len(properties[0])):
    if properties[i][0]==zipcodes:
        columnzip=i
for i in range(len(zipcodes[0])):
    if zipcodes[0][i]==properties:
print("Zipcode {}".format(zipcodes), "Count {}".format(count), "Average {}",format(average))