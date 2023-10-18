rows, cols= tuple ([int(x) for x in input("Enter the number of rows and columns: ").split()])
data=[]
for i in range(rows):
    values = input("Enter a line of data: ").split()
    data.append([int (x) for x in values])
for row in data:
    for value in row:
        print(value, end=" ")
        print()
rowH, colH = 0, 0
for i in range (rows):
    for j in range(cols):
        if data[i][j]>data[rowH][colH]:
            rowH, colH = i, j
print("The maximum value", data[rowH][colH],"occured in row", rowH, "and column", colH)