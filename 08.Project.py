import requests
response = requests.get('https://www.usconstitution.net/const.txt')
filestring = response.text
filestringlist = filestring.split("\n")
while t != ' ':
    for i in range (len(filestringlist)):
        if filestringlist[i].find(t) != -1:
            print(filestringlist[i])
    t= input("Enter search term: ")
for i in 