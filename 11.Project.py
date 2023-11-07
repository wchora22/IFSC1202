from math import pi
class Student():
    def __init__(self,firstname,lastname,tnumber):
        self.firstname=firstname
        self.lastname=lastname
        self.tnumber=tnumber
        self.grades= grades
    
    def RunningAverage(self):
    list = []
    x=0
    for x in range(len(self.scores)):
        if(self.scores[x]=='\n'):
            a=1
            
        elif(self.scores[x]=='\n'):
            a=2
        else:
            list.append(self.scores[x])

    avg=sum(list)/len(list)

    return avg