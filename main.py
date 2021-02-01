from Menu import Menu
from SimpleMenu import SimpleMenuItem
def test():
    print("ТЕСТ")
glavnoeMenu=Menu("Главное меню",0)
glavnoeMenu.additem(0,"Пункт_1",test)
subMenu = glavnoeMenu.addSubMenu("Пункт_2",2)
subMenu.additem(0,"Пункт_3",test)
subMenu.additem(0,"Пункт_4",test)
#glavnoeMenu.item[1].additem(0,"Назад",test)
#glavnoeMenu.additem(3,"Выход",test)
glavnoeMenu.execute()