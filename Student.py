class Student:
    def __init__(self,first_name,midle_name,last_name,group):
        self.first_name=first_name
        self.midle_name=midle_name
        self.last_name=last_name
        self.group=group
        self.marks={}
    def print_long(self):
        print(f"{self.first_name} {self.midle_name} {self.last_name}")
        print(f"Группа : {self.group}")
        self.printSubjects()
    def print_short(self):
        print(f"{self.first_name} {self.last_name}, {self.group}")
    def printSubjects(self):
        if len(self.marks)!=0:
            print("Список предметов: ")
            for key in self.marks.keys():
               print(f"{key}:{self.marks[key]}")
        else: print("список пуст")
        