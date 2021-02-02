from Singleton import Singleton
from Student import Student
class Edit_context(metaclass=Singleton):
    def __init__ (self):
        self.student=None
    #def get_instanse(self):
