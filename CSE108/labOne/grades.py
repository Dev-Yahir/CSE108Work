
def createStudent():
    checkName = False
    while not checkName:
        name = input("What is the name of the student? ")
        if name in Student.class_dict:
            print("Student already exists. Please enter a different name.")
        elif name == "" or len(name.split()) < 2:
            print("First and last name must be entered.")
        if(len(name.split()) == 2):
            checkName = True
    checkGrade = False
    while not checkGrade:
        try:
            grade = int(input("What is the Students grade? "))
        except ValueError:
            print("Grade must be a number.")
            continue
        if grade not in range(0, 101):
            print("Grade must be between 0 and 100.")
        elif not isinstance(grade, int):
            print("Grade must be a number.")
        else:
            checkGrade = True
    student = Student(name, grade)
    student.class_dict[name] = grade
    return student

class Student:
    class_dict = {}
    def __init__(self, name, grade = None):
        fullName = list(name.split())
        fname = fullName[0]
        lname = fullName[1]
        self.firstname = fname
        self.lastname = lname
        self.grade = grade
        self.class_dict[name] = grade
    
    def printInfo(self):
        print("Name: ", self.firstname, self.lastname, "Grade: ", self.grade)

    def setGrade(self, grade):
        self.grade = grade

    def removeGrade(self):
        self.grade = None

    def printDict(self):
        print(self.class_dict)

stud1 = createStudent()

stud1.printInfo()
stud1.setGrade(100)
stud1.printInfo()
stud1.removeGrade()
stud1.printInfo()
stud1.printDict()

stud2 = createStudent()

stud2.printInfo()
stud2.setGrade(50)
stud2.printInfo()
stud2.removeGrade()
stud2.printInfo()
stud2.printDict()