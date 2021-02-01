from StudentVisitor import StudentVisitor

class LowAchiverVisitor(StudentVisitor):
    def start_visit(self):
        self.has_students=False

    def visit_student(self,number,student):
        self.low_student=False
        for key in student.marks.keys():
            if student.marks[key]==2:
                self.low_student=True
        if self.low_student:
            self.has_students = True
            print(f"=== {number} ===")
            student.print_long()
        
    def finish_visit(self):
        if not self.has_students:
            print("Неуспевающих в базе данных нет")