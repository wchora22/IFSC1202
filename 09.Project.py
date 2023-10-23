a = []
numbersfile = open("09.Project Distances.csv", 'r')
x = numbersfile.readline().strip()
y=x.split(",")
a.append(y)
x=numbersfile.readline().strip()
while x != "":
	y = x.split(",")
	a.append(y)
	x = numbersfile.readline().strip()
for i in range(len(a)):
    for j in range(len(a[i])):
        print("{:>10s}".format(a[i][j]), end='')
    print()
fromcity = str(input("Enter from City: "))
tocity = str(input("Enter to City: "))
fromrow=-1
tocolumn=-1
for i in range(len(a)):
    if a[0][i]==fromcity:
        fromrow=i
for i in range(len(a[0])):
     if a[i][0]==tocity:
        tocolumn=i
if fromrow==-1:
    print("Invalid from City")
if tocolumn==-1:
    print("Invalid to City")
if fromrow!=-1 and tocolumn!=-1:
    print("{} to {} - {} miles".format(fromcity, tocity, a[fromrow][tocolumn]))