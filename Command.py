from StudentVisitor import StudentVisitor
from Stud_Registry import StudentRegistry
from Student import Student
def ListStudentsCommand():
  v = DetailedPrintVisitor()
  StudentRegistry().visit_students(v)

def AddStudentCommand():
  first_name=input("Введите фамилию")
  midle_name=input("Введите отчество")
  last_name=input("Введите имя")
  group=input("Введите группу")
  NewStudent=Student(first_name,midle_name,last_name,group)
  StudentRegystry().addStudent(NewStudent)

def ShowHightAchiverCommand():
  s = HightAchiverVisitor()
  StudentRegistry().visit_students(s)

def ShowLowAchiverCommand():
  s = LowAchiverVisitor()
  StudentRegistry().visit_students(s)

def DeliteStudentCommand():
  BrifShow= BriefPrintVisitor()
  StudentRegistry().visit_students(BrifShow)
  number=int(input("Введите номер студента"))
  while number < 1 or len(StudentRegistry().students) < number
    number=input("Такого студента нет, введите номер студента")
  ready=int(input("Удалить студента номер {number}\n Введите 1-да 2-нет"))
  while ready !=1 and ready !=2:
    ready=input("Такого варината нет \nУдалить студента номер {number}\n Введите 1-да 2-нет")
  if ready ==1:
   StudentRegistry().removeStudent(number)