from Singleton import Singleton
import os
from Student import Student
#from StudentVisitor import StudentVisitor
#from DetailedPrintVisitor import DetailedPrintVisitor
#from Menu import Menu
#from SimpleMenu import SimpleMenuItem
import json
class StudentRegistry(metaclass=Singleton):
    def __init__(self):
        self.students=[]
        self.save()
        self.load()
        
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
    def save(self):
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

    def load (self):
        if os.path.exists("DocSave.json"):
            with open ("DocSave.Json","r") as f:
                saveStudents = json.load(f)
                for i, json_student in enumerate(saveStudents):
                    student = Student(json_student["First Name"], json_student["Midl Name"], json_student["Last Name"], json_student["Group"])
                    student.marks=json_student["Marks"]
                    self.students.append(student)