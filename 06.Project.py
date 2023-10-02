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
            recordcount +=1 
            outputfile.write(line)
            mergerecord+=1
            line = mergefile.readline()
        outputfile.write("\n")
        mergefile.close()
    else:
        inputrecord+=1
        outputfile.write(line)
        recordcount +=1
    line = inputfile.readline()
inputfile.close()
outputfile.close()
print("{} input file records".format(inputrecord))
print("{} merge file records".format(mergerecord))
print("{} output file records".format(recordcount))