from Singleton import Singleton
from Student import Student
#from Menu import Menu
#from SimpleMenu import SimpleMenuItem
def test():
    print("test")
class StudentRegistry(metaclass=Singleton):
    def __init__(self):
        self.students=[]
        
    def addStudent(self,student):
        self.students.append(student)

    def removeStudent(self,number):
        del self.students[number]

    def getStudent(self,number):
        return self.students[number]

    def getStudentCount(self):
        return len(self.students)

    def visit_students(self, visitor):
        visitor.start_visit()
        for i, student in enumerate(self.students):
          visitor.visit_student(i, student)
        visitor.finish_visit()
        ##while number > len() or number < 1:
        #self.students[number].printLong()
        #send=int(input("Редактировать студента ? 1:да 2:нет"))
        #while send !=1 or send !=2:
        #    send=int(input("Редактировать студента ? 1:да 2:нет"))
        #if send ==1:
        #    studMenu=Menu.addSubMenu("Редактирование студента",1)
        #    studMenu.additem(number,"Редактировать фамилию",test)
        #    studMenu.additem(number,"Редактировать Имя",test)
        #    studMenu.additem(number,"Редактировать Отчество",test)
        #    zaprosPredmetov=int(input("Заполнить или изменить предметы и оценки? 1-да 2-нет"))
            #if zaprosPredmetov==1:
                #predmetMenu=studMenu.addSubMenu("Редактирование списка предметов",0)
                #predmetMenu.


            #self.students[number]=self.addStudent(student)
        
