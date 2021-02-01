from Stud_Registry import StudentRegistry
from abc import ABCMeta, abstractmethod

class StudentVisitor(metaclass=ABCMeta):
    @abstractmethod
    def start_visit(self):
        pass

    @abstractmethod
    def visit_student(self):
        pass

    @abstractmethod
    def finish_visit(self):
        pass