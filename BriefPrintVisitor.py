from StudentVisitor import StudentVisitor

class BriefPrintVisitor(StudentVisitor):
  def start_visit(self):
    self.has_students = False

  def visit_student(self, number, student):
    print(f" {number+1}.",end="")
    student.print_short()
    self.has_students = True

  def finish_visit(self):
    if not self.has_students:
      print("Студентов в базе данных нет")