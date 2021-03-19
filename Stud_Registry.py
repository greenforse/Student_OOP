from Singleton import Singleton
from Student import Student
#from StudentVisitor import StudentVisitor
#from DetailedPrintVisitor import DetailedPrintVisitor
#from Menu import Menu
#from SimpleMenu import SimpleMenuItem
import json
class StudentRegistry(metaclass=Singleton):
    def __init__(self):
        self.students=[]
        self.saveLoad()
        
    def addStudent(self,student):
        self.students.append(student)

    def removeStudent(self,number):
        del self.students[number-1]

    def getStudent(self,number):
        return self.students[number-1]

    def getStudentCount(self):
        return len(self.students)

    def visit_students(self, visitor):
        visitor.start_visit()
        for i, student in enumerate(self.students):
          visitor.visit_student(i, student)
        visitor.finish_visit()
    def saveLoad(self):
        if len(self.students)!=0:
            saveStudents=[]
            for i, student in enumerate(self.students):
                saveStudent={}
                saveStudent["First Name"] = student.first_name
                saveStudent["Midl Name"] = student.midle_name
                saveStudent["Last Name"] = student.last_name
                saveStudent["Group"] = student.group
                marks={}
                for i, mark in student.marks.items():
                    marks[i]=mark
                saveStudent["Marks"] = marks
                saveStudents.append(saveStudent)
            json_str= json.dumps(saveStudents)
            with open ("DocSave.json","w") as f:
                f.write(json_str)
       