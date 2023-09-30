inputfilename = "06.Project Input File.txt"
outputfilename = "06.Project Output File.txt"
recordcount = 0
inputrecord=0
mergerecord=0
inputfile = open(inputfilename, 'r')
outputfile = open(outputfilename, 'w')  
line = inputfile.readline()
while line != '':
    if line == "**Insert Merge File Here**\n":
        mergefilename= "06.Project Merge File.txt"
        mergefile=open(mergefilename, 'r')
        line= mergefile.readline()
        while line != "":
            outputfile.write(line)
            line = mergefile.readline()
        outputfile.write("\n")
        mergefile.close()
    else:
        outputfile.write(line)
    recordcount += 1
    inputrecord += 1
    mergerecord += 1
    line = inputfile.readline()
inputfile.close()
outputfile.close()
print("{} input files".format(inputrecord))
print("{} merge files".format(mergerecord))
print("{} output files".format(recordcount))