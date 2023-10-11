def DDMMSStoDecimal(degrees, minutes, seconds):
    decimaldegrees= degrees+(minutes/60)+(seconds/3600)
    return decimaldegrees
def ParseDDMMSS(ddmmss):
    degreepos= ddmmss.find(chr(176))
    degrees=float(ddmmss[:degreepos])
    minutepos=ddmmss.find("'")
    minutes=float(ddmmss[degreepos+1:minutepos])
    secondpos = ddmmss.find('"')
    seconds = float(ddmmss[minutepos+1:secondpos])
    return degrees, minutes, seconds
inputfilename= "07.Project Angles Input.txt"
outputfilename= "07.Project Angles Output.txt"
records=0
inputfile = open(inputfilename, 'r')
outputfile= open(outputfilename, 'w')
line =inputfile.readline()
while line != '':
    degrees, minutes, seconds = ParseDDMMSS(line)
    decimaldegree = DDMMSStoDecimal(degrees, minutes, seconds)
    outputfile.write(str(decimaldegree)+ "\n")
    records = records+1
    line = inputfile.readline()
inputfile.close()
outputfile.close()
print(records, "records processed")