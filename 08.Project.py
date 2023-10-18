import requests
response = requests.get('https://www.usconstitution.net/const.txt')
filestring = response.text
filestringlist = filestring.split("\n")
t= input("Enter search term: ")
while t != ' ':
    for i in range (len(filestringlist)):
        if filestringlist[i].find(t) != -1:
 #           print(filestringlist[i])
            for j in range(i,0,-1):
                if filestringlist[j] == "":
                    top = j
                    break
            for k in range(i,len(filestringlist)):
                if filestringlist[k]== "":
                    bottom = k
                    break
            
            for l in range(top,bottom):
                print("Line {}: {}".format(l,filestringlist[l]))
    t= input("Enter search term: ")