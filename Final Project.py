class User():
    def __init__(self,username,password):
        self.Username=username
        self.Password=password
class Userlist():
    def __init__(self,filename):
        self.Userlist=[]
        self.filename=filename
    def ReadUserFile(self):
        userfile=open(self.filename,"r")
        line=userfile.readline()
        while line != "":
            x=line.split(",")
            userobject=User(x[0].strip(), x[1].strip())
            self.Userlist.append(userobject)
            line=userfile.readline()
    def WriterUserFile(self):
        userfile=open(self.filename, "w")
    def DisplayUserlist(self):
        for i in range(len(self.Userlist)):
            print(self.Userlist[i].Username,self.Userlist[i].Password)
    def FindUsername(username):

    def ChangePassword(password):

    def AddUser(username,password):

    def DeleteUser(username):

    def Strength(password):

MyUserlist=Userlist("Final Project Passwords.txt")
MyUserlist.ReadUserFile()
MyUserlist.DisplayUserlist()
MyUserlist.WriterUserFile()