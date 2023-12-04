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
        for i in range(len(self.Userlist)):
            userfile.write(self.Userlist[i].Username + "," + self.Userlist[i].Password + "\n")
        userfile.close()
    def DisplayUserlist(self):
        for i in range(len(self.Userlist)):
            print(self.Userlist[i].Username,self.Userlist[i].Password)
    def FindUsername(self,username):
        for i in range(len(self.Userlist)):
            if self.Userlist[i].Username==username:
                return i
        return -1
    def ChangePassword(self, username,password):
        index=self.FindUsername(username)
        if index!=-1:
            self.Userlist[index].Password=password
    def AddUser(self,username,password):
        index=self.FindUsername(username)
        if index==-1:
            self.Userlist.append(User(username,password))
        return
    def DeleteUser(self, username):
        index=self.FindUsername(username)
        if index!=-1:
            del self.Userlist[index]
        return
    def Strength(self, password):
        strength=len(password)
        return strength
MyUserlist=Userlist("Final Project Passwords.txt")
MyUserlist.ReadUserFile()

print("1. Add a New User")
print("2. Delete an Existing User")
print("3. Change Password on an Existing User")
print("4. Display All Users")
print("5. Save Changes to File")
print("6. Quit")
choice=""
while choice!="6":
    choice=input("Enter Selection:")
    if choice =="1":
        username= input("Enter Username:")
        index=MyUserlist.FindUsername(username)
        if index!=-1:
            print ("Username already exist")
        else:
            password= input("Enter Password:")
            strength=MyUserlist.Strength(password)
            if strength >=5:
                MyUserlist.AddUser(username,password)
    if choice =="2":
        username= input("Enter username:")
        index=MyUserlist.FindUsername(username)
        if index==-1:
            print("Username Not Found")
        else:
            MyUserlist.DeleteUser(username)
    if choice=="3":
        username = input("Enter Username:")
        index=MyUserlist.FindUsername(username)
        if index==-1:
            print("Username Not Found")
        else:
            password=input("Enter Password:")
            strength=MyUserlist.Strength(password)
            if strength >=5:
                MyUserlist.ChangePassword(username,password)
                print ("Password Changed")

    if choice=="4":
        MyUserlist.DisplayUserlist()

    if choice=="5":
        MyUserlist.WriterUserFile()