class Student():
    def __init__(self,firstname,lastname,tnumber, scores):
        self.firstname=firstname
        self.lastname=lastname
        self.tnumber= tnumber
        self.scores= scores

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
def TotalAverage(self):
    list=[]
    x=0
    for x in range(len(self.scores)):
        if(self.scores[x]==''):
            list.append(0)
        elif(self.scores[x]=='\n'):
            list.append(0)
        else:
            list.append(self.score[x])
    
    avg= sum(list)/len(list)
    print(list)
    return avg

def Lettergrade(self, Student):
    avg= Student
    avg = round(avg)
    if(avg>=90):
        grade="A"
    elif(avg>=80 and avg<90):
        grade="B"
    elif(avg>=70 and avg<80):
        grade="C"
    elif(avg>=60 and avg<70):
        grade="D"
    elif(avg<60):
        grade="F"
    return grade

scorefile=open("10.Project Student Scores.txt",'r')