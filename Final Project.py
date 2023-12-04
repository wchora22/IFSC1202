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
        print()
    def DisplayUserlist(self):
        for i in range(len(self.Userlist)):
            print(self.Userlist[i].Username,self.Userlist[i].Password)
    def FindUsername(self,username):
        for i in range(self.Userlist):
            if self.Userlist[i].Username==username:
                return i
        return -1
    def ChangePassword(self, username,password):
        index=self.FindUsername(username)
        if index==-1:
            print("Username Not Found")
        else:
            password=input("Enter Password:")
            strength=self.Strength(password)
            if strength >=5:
                self.Userlist[i].Password=password
    def AddUser(self,username,password):
        return
    def DeleteUser(self, username):
        return
    def Strength(self, password):
        return 5
MyUserlist=Userlist("Final Project Passwords.txt")
MyUserlist.ReadUserFile()
MyUserlist.DisplayUserlist()
