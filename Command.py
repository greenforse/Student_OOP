from StudentVisitor import StudentVisitor
from Stud_Registry import StudentRegistry
from Student import Student
from Edit_context import Edit_context
from DetailedPrintVisitor import DetailedPrintVisitor
def ListStudentsCommand():
  v = DetailedPrintVisitor
  StudentRegistry.visit_students(v)

def AddStudentCommand():
  first_name=input("Введите фамилию")
  midle_name=input("Введите отчество")
  last_name=input("Введите имя")
  group=input("Введите группу")
  NewStudent=Student(first_name,midle_name,last_name,group)
  StudentRegistry().addStudent(NewStudent)

def ShowHightAchiverCommand():
  s = StudentVisitor().HightAchiverVisitor()
  StudentRegistry().visit_students(s)

def ShowLowAchiverCommand():
  s = StudentVisitor().LowAchiverVisitor()
  StudentRegistry().visit_students(s)

def DeleteStudentCommand():
  BrifShow= StudentVisitor().BriefPrintVisitor()
  StudentRegistry().visit_students(BrifShow)
  number=int(input("Введите номер студента"))
  while number < 1 or len(StudentRegistry().students) < number:
    number=input("Такого студента нет, введите номер студента")
  ready=int(input("Удалить студента номер {number}\n Введите 1-да 2-нет"))
  while ready !=1 and ready !=2:
    ready=input("Такого варината нет \nУдалить студента номер {number}\n Введите 1-да 2-нет")
  if ready ==1:
   StudentRegistry().removeStudent(number)

def SelectStudentCommand():
  SelectShow= StudentVisitor().BriefPrintVisitor()
  StudentRegistry().visit_students(SelectShow)
  SelectNumber=int(input("Введите номер студента"))
  while SelectNumber < 1 or len(StudentRegistry().students) < SelectNumber:
    SelectNumber=int(input("Такого студента нет, введите номер студента: "))
  Edit_context().student=StudentRegistry().getStudent(SelectNumber)

def ShowSelectCommand():
  Edit_context().student.print_long()

def DeselectStudentCommand():
  Edit_context().student=None

def EditFirstNameCommand():
  fname=input("Введите новое имя")
  Edit_context().student.insert(0,fname)
  del Edit_context().studen[1]

def EditMidleNameCommand():
  MName=input("Введите новую фамилию")
   Edit_context().student.insert(1,MName)
   del Edit_context().studen[2]
  
def EditLastNameCommand():
  LName=input("Введите новое отчесво")
   Edit_context().student.insert(2,LName)
   del Edit_context().studen[3]

def EditGroupCommand():
  group=input("Введите новую группу")
   Edit_context().student.insert(3,group)
   del Edit_context().studen[4]

def AddMarkCommand():
  mark=input("Введите предмет: ")
  if mark not in Edit_context.student.marks:
    score=int(input("Введите оценку: "))
    Edit_context.student.marks[mark]=score
  else print("Ошибка: такой предмет уже есть")

def EditMarkCommand():
  mark=input("Введите предмет: ")
  if mark  in Edit_context.student.marks:
    score=int(input("Введите оценку: "))
    Edit_context.student.marks[mark]=score
  else print("Ошибка: такой предмета нет")

def DeleteMarkCommand():
  mark=input("Введите предмет для удаления: ")
  if mark  in Edit_context.student.marks:
    del Edit_context.student.marks[mark]
  else print("Ошибка: такой предмета нет")
