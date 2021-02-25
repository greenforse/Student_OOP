from Menu import Menu
from SimpleMenu import SimpleMenuItem
import Command
def test():
    print("ТЕСТ")
glavnoeMenu=Menu("Главное меню",0)
#glavnoeMenu.additem(0,"Пункт_1",Command.ListStudentsCommand())

glavnoeMenu.additem(1,"Список студентов",Command.ListStudentsCommand)
subMenu = glavnoeMenu.addSubMenu("Редактировать студента",2)
subMenu.set_startup_command(Command.SelectStudentCommand)
subMenu.set_before_select_command(Command.ShowSelectCommand)
subMenu.set_tear_down_command(Command.DeselectStudentCommand)
subMenu.additem(1,"Удалить студента",Command.DeleteStudentCommand)
#subMenu.additem(0,"Пункт_3",test)
#subMenu.additem(0,"Пункт_4",test)
#glavnoeMenu.item.append(subMenu)
#glavnoeMenu.item[1].additem(0,"Назад",test)
#glavnoeMenu.additem(3,"Выход",test)

glavnoeMenu.execute()