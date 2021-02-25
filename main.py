from Menu import Menu
from SimpleMenu import SimpleMenuItem
import Command
def test():
    print("ТЕСТ")
glavnoeMenu=Menu("Главное меню",0)
#glavnoeMenu.additem(0,"Пункт_1",Command.ListStudentsCommand())

glavnoeMenu.additem(1,"Список студентов",Command.ListStudentsCommand())
#subMenu.additem(0,"Пункт_3",test)
#subMenu.additem(0,"Пункт_4",test)
#glavnoeMenu.item.append(subMenu)
#glavnoeMenu.item[1].additem(0,"Назад",test)
#glavnoeMenu.additem(3,"Выход",test)

glavnoeMenu.execute()