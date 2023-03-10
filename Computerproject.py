# define a class to represent a student
class Student:
  def _init_(self, name, roll_number, marks):
    self.name = name
    self.roll_number = roll_number
    self.marks = marks

# define a class to represent an examination
class Examination:
  def _init_(self, name, max_marks):
    self.name = name
    self.max_marks = max_marks

# define a class to represent a student examination portal
class StudentExaminationPortal:
  def _init_(self):
    # create an empty list to store students
    self.students = []
    # create an empty list to store examinations
    self.examinations = []

  def add_student(self, student):
    self.students.append(student)

  def add_examination(self, examination):
    self.examinations.append(examination)

  def get_student_marks(self, student):
    # find the student in the list of students
    found_student = None
    for s in self.students:
      if s.roll_number == student.roll_number:
        found_student = s
        break

    # if the student is not found, return None
    if found_student is None:
      return None

    # create a dictionary to store the examination name and marks for the student
    marks = {}
    for examination in self.examinations:
      # find the marks for the examination in the student's marks list
      found_marks = None
      for m in found_student.marks:
        if m['examination'] == examination.name:
          found_marks = m
          break

      # if marks are not found for the examination, set it to 0
      if found_marks is None:
        marks[examination.name] = 0
      else:
        marks[examination.name] = found_marks['marks']

    return marks

# create 6 student
S1 = Student("John Stan", 1, [{"examination": "exam1", "marks": 90}, {"examination": "exam2", "marks": 80}])
S2 = Student("Alex Standall", 2, [{"examination": "exam1","marks": 85}, {"examination": "exam2", "marks":89}])
S3 = Student("Hannah Baker", 3, [{"examination": "exam1","marks": 83}, {"examination": "exam2", "marks":93}])
S4 = Student("Clay Jensen", 4, [{"examination": "exam1","marks": 89}, {"examination": "exam2", "marks":78}])
S5 = Student("Hermione Granger", 5, [{"examination": "exam1","marks": 93}, {"examination": "exam2", "marks":88}])
S6 = Student("Harry Porter", 6, [{"examination": "exam1","marks": 87}, {"examination": "exam2", "marks":97}])

# create an examination
e1 = Examination("exam1", 100)
e2 = Examination("exam2", 100)

# create a student examination portal
sep = StudentExaminationPortal()

# add the student and examination to the portal
sep.add_student(S1,S2,S3,S4,S5,S6)
sep.add_examination(e1)
sep.add_examination(e2)

# get the marks for the student
marks = sep.get_student_marks(s)
print(marks)  # output: {'exam1': 90, 'exam2': 80}