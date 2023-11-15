#from math import pi
class Student():
    def __init__(self,firstname,lastname,tnumber):
        self.FirstName=firstname
        self.LastName=lastname
        self.TNumber=tnumber
        self.Grades=[]
    def RunningAverage(self):
        total= 0
        count = 0
        for x in range(len(self.Grades)):
            if(self.Grades[x]!=''):
                total = total + float(self.Grades[x])
                count = count + 1
        avg=total/count
        return avg
    def TotalAverage(self):
        total= 0
        count=0
        for x in range(len(self.Grades)):
            if(self.Grades[x]!=''):
                total = total + float(self.Grades[x])
            count = count + 1
        avg=total/count
        return avg
    def LetterGrade(self):
        avg=self.TotalAverage()
        if(avg>=90):
            return "A"
        elif(avg>=80 and avg<90):
            return "B"
        elif(avg>=70 and avg<80):
            return "C"
        elif(avg>=60 and avg<70):
            return "D"
        elif(avg<60):
            return "F"
class StudentList:
    def __init__(self):
        self.StudentList=[]
    def add_student(self, FirstName, LastName, TNumber):
        student= Student(FirstName, LastName, TNumber)
        self.StudentList.append(student)
    def find_student(self,TNumber):
        for index, student in enumerate(self.StudentList):
            if student.TNumber==TNumber:
                return index
        return -1
    def print_student_list(self):
        print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'.format('First', 'Last', 'ID', 'Running', 'Semester', 'Letter'))
        print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'.format('Name', 'Name', 'Number', 'Average', 'Average', 'Grade' ))
        print('-' *12, '-' *12, '-' *12, '-' *12, '-' *12, '-' *12)
        for student in self.StudentList:
            print('{:<12} {:<12} {:<12} {:<12.2f} {:<12.2f} {:<12}'.format(student.FirstName, student.LastName, student.TNumber, student.RunningAverage(), student.TotalAverage(), student.LetterGrade()))

    def add_student_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                FirstName, LastName, TNumber = line.strip().split(',')
                self.add_student(FirstName, LastName, TNumber)
    def add_grades_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                TNumber, grades= line.strip().split(',')
                index = self.find_student(TNumber)
                if index !=-1:
                    self.StudentList[index].Grades.append(grades)
if __name__ == "__main__":
    student_list = StudentList()
    student_list.add_student_from_file("11.Project Students.txt")
    student_list.add_grades_from_file("11.Project Scores.txt")
    student_list.print_student_list()