from StudentVisitor import StudentVisitor

class HigtAchiverVisitor(StudentVisitor):
    def start_visit(self):
        self.has_students=False

    def visit_student(self,number,student):
        
        self.hight_student=True

        if len(student.marks)!=0:
            for key in student.marks.keys():
                if student.marks[key]!=5 :
                    self.hight_student=False
            if self.hight_student:
                print(f"=== {number+1} ===")
                student.print_long()
                self.has_students = True

    def finish_visit(self):
        if not self.has_students:
            print("Отличников в базе данных нет")
