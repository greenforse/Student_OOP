from StudentVisitor import StudentVisitor
from Stud_Registry import StudentRegistry
def ListStudentsCommand():
  v = DetailedPrintVisitor()
  StudentRegistry().visit_students(v)

def AddStudentCommand():
  first_name=input("Введите фамилию")
  midle_name=input("Введите отчество")
  last_name=input("Введите имя")
  group=input("Введите группу")
  NewStudent=Studen(first_name,midle_name,last_name,group)
  StudentRegystry().addStudent(NewStudent)

def ShowHightAchiverCommand():
  s = HightAchiverVisitor()
  StudentRegistry().visit_students(s)

def ShowLowAchiverCommand():
  s = LowAchiverVisitor()
  StudentRegistry().visit_students(s)

def DeliteStudentCommand(number):
  StudentRegistry().removeStudent(number)
