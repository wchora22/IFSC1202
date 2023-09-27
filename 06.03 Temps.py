file = open("06.03 FTemps.txt", "r")
records = 0
for F in file:
    C = (float(F)-32)*5/9
    C = round(C,1)
    f = open("06.03 CTemps.txt", "a")
    f.write(str(C))
    f.write('\n')
    f.close()
    records = records+1
print(str(records)+" records written")