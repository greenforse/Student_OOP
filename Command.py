#from StudentVisitor import StudentVisitor
from Stud_Registry import StudentRegistry
from Student import Student
from Edit_context import Edit_context
from DetailedPrintVisitor import DetailedPrintVisitor
from BriefPrintVisitor import BriefPrintVisitor
from HigtAchiverVisitor import HigtAchiverVisitor
from LowAchiverVisitor import LowAchiverVisitor

def ListStudentsCommand():
  v = DetailedPrintVisitor()#последнее изменение
  StudentRegistry().visit_students(v)

def AddStudentCommand():
  first_name=input("Введите фамилию: ")
  midle_name=input("Введите отчество: ")
  last_name=input("Введите имя: ")
  group=input("Введите группу: ")
  NewStudent=Student(first_name,midle_name,last_name,group)
  #NewStudent=(first_name,midle_name,last_name,group)
  StudentRegistry().addStudent(NewStudent)
  StudentRegistry().saveLoad()

def ShowHightAchiverCommand():
  s = HigtAchiverVisitor()
  StudentRegistry().visit_students(s)

def ShowLowAchiverCommand():
  s = LowAchiverVisitor()
  StudentRegistry().visit_students(s)

def DeleteStudentCommand():
  BrifShow = BriefPrintVisitor()
  StudentRegistry().visit_students(BrifShow)
  number=int(input("Введите номер студента"))
  while number < 1 or len(StudentRegistry().students) < number:
    number=input("Такого студента нет, введите номер студента")
  ready=int(input(f"Удалить студента номер {number}\n Введите 1-да 2-нет: "))
  while ready !=1 and ready !=2:
    ready=input(f"Такого варината нет \nУдалить студента номер {number}\n Введите 1-да 2-нет")
  if ready ==1:
   StudentRegistry().removeStudent(number)
   StudentRegistry().save()

def SelectStudentCommand():
  SelectShow = BriefPrintVisitor()
  StudentRegistry().visit_students(SelectShow)
  SelectNumber=int(input("Введите номер студента"))
  while SelectNumber < 0 or len(StudentRegistry().students) < SelectNumber: # Заменил в условии 1 на 0
    SelectNumber=int(input("Такого студента нет, введите номер студента: "))
  Edit_context().student=StudentRegistry().getStudent(SelectNumber)

def ShowSelectCommand():
  Edit_context().student.print_long()#Изменение 1 ()

def DeselectStudentCommand():
  Edit_context().student=None #Изменение 2 ()

def EditFirstNameCommand():
  fname=input("Введите новую фамилию: ")
  #EditFName=Edit_context().student
  Edit_context().student.first_name = fname
  StudentRegistry().save()
  #EditFName.insert(0,fname)
  #del Edit_context().student[1]

def EditMidleNameCommand():
  MName=input("Введите новое Отчество: ")
  Edit_context().student.midle_name = MName
  StudentRegistry().save()
  #del Edit_context().student[2]

def EditLastNameCommand():
  LName=input("Введите новое имя: ")
  Edit_context().student.last_name = LName
  StudentRegistry().save()
  #del Edit_context.student[3]

def EditGroupCommand():
  group=input("Введите новую группу")
  Edit_context().student.insert(3,group)
  del Edit_context.student[4]
  StudentRegistry().save()

def AddMarkCommand():
  mark=input("Введите предмет: ")
  if mark not in Edit_context().student.marks:
    score=int(input("Введите оценку: "))
    Edit_context().student.marks[mark]=score
    StudentRegistry().save()
  else: print("Ошибка: такого предмет уже есть")

def EditMarkCommand():
  mark=input("Введите предмет: ")
  if mark  in Edit_context().student.marks:
    score=int(input("Введите оценку: "))
    Edit_context().student.marks[mark]=score
    StudentRegistry().save()
  else: print("Ошибка: такого предмета нет")

def DeleteMarkCommand():
  mark=input("Введите предмет для удаления: ")
  if mark  in Edit_context().student.marks:
    YN=int(input("Вы действительно хотите удалить предмет 1-да 2-нет"))
    if YN == 1 :
      del Edit_context().student.marks[mark]
      StudentRegistry().save()
    if YN == 2:
      pass
    else: print("нет такого варианта ответа")
    #while YN!=1 or YN!=2:
    #  YN=int(input("Вы действительно хотите удалить предмет 1-да 2-нет"))
    #  if mark  in Edit_context().student.marks:
    #    YN=int(input("Вы действительно хотите удалить предмет 1-да 2-нет"))
    #    if YN == 1 :
    #      del Edit_context().student.marks[mark]
  else: print("Ошибка: такой предмета нет")
