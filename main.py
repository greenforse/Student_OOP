import os
import json
from Menu import Menu
from SimpleMenu import SimpleMenuItem
import Command
from Student import Student
from Stud_Registry import StudentRegistry
#if os.path.exists("DocSave.json"):
#    with open ("DocSave.Json","r") as f:
#        saveStudents = json.load(f)
#        for i, json_student in enumerate(saveStudents):
#            student = Student(json_student["First Name"], json_student["Midl Name"], json_student["Last Name"], json_student["Group"])
#            student.marks=json_student["Marks"]
#            StudentRegistry().students.append(student)
def test():
    print("ТЕСТ")
glavnoeMenu=Menu("Главное меню",0)
#glavnoeMenu.additem(0,"Пункт_1",Command.ListStudentsCommand())

glavnoeMenu.additem(1,"Список студентов",Command.ListStudentsCommand)
AddStud=glavnoeMenu.additem(2,"Добавить студента",Command.AddStudentCommand )
glavnoeMenu.additem(3,"Удалить студента",Command.DeleteStudentCommand)
#subMenu = glavnoeMenu.addSubMenu("Удалить студента",3)
#subMenu.set_startup_command(Command.SelectStudentCommand)
#subMenu.set_before_select_command(Command.ShowSelectCommand)
#subMenu.set_tear_down_command(Command.DeselectStudentCommand)
#subMenu.additem(1,"Удалить студента",)

editStudents=glavnoeMenu.addSubMenu("Редактировать студента",4)
editStudents.set_startup_command(Command.SelectStudentCommand)
editStudents.set_before_select_command(Command.ShowSelectCommand)
editStudents.set_tear_down_command(Command.DeselectStudentCommand)
editStudents.additem(1,"Изменить фамилию",Command.EditFirstNameCommand)
editStudents.additem(2,"Изменить имя",Command.EditMidleNameCommand)
editStudents.additem(3,"Изменить отчество",Command.EditLastNameCommand)
editStudents.additem(4,"Изменить группу",Command.EditGroupCommand)
editStudents.additem(5,"добавить оценку",Command.AddMarkCommand)
editStudents.additem(6,"Изменить оценку",Command.EditMarkCommand)
editStudents.additem(6,"Удалить оценку",Command.DeleteMarkCommand)

HighShow=glavnoeMenu.additem(5,"Показать отличников",Command.ShowHightAchiverCommand)

LowShow=glavnoeMenu.additem(6,"Показать неуспевающих",Command.ShowLowAchiverCommand)


#subMenu.additem(0,"Пункт_3",test)
#subMenu.additem(0,"Пункт_4",test)
#glavnoeMenu.item.append(subMenu)
#glavnoeMenu.item[1].additem(0,"Назад",test)
#glavnoeMenu.additem(3,"Выход",test)

glavnoeMenu.execute()