class CourseInfo:
    def __init__(self, courseDep, courseNum, courseName, courseCredits, courseBegTime, courseEndTime, courseLecDays, courseAvgGrade, cnum):
        self.courseDep = courseDep
        self.courseNum = courseNum
        self.courseName = courseName
        self.courseCredits = courseCredits
        self.courseLecDays = courseLecDays
        self.courseBegTime = courseBegTime
        self.courseEndTime = courseEndTime
        self.courseAvgGrade = courseAvgGrade
        self.cnum = cnum

    def printInfo(self):
        print(f"COURSE {self.cnum}: {self.courseDep} {self.courseNum} : {self.courseName}")
        print(f"Number of Credits: {self.courseCredits}")
        print(f"Days of Lectures: {self.courseLecDays}")
        print(f"Lecture Time: {self.courseBegTime} - {self.courseEndTime}")
        print(f"Stat: on average, students get {self.courseAvgGrade}% in this course")

def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return None  # File not found

file_path = 'classesInput.txt'
lines = read_file_lines(file_path)

if lines is None:
    print("Error: File not found.")
else:
    try:
        numClasses = int(lines[0])  # First line contains the number of courses
        courses = []

        for i in range(numClasses):
            start_idx = 1 + i * 8  # Calculate the starting index for each course data block
            course = CourseInfo(
                lines[start_idx],      # Department
                lines[start_idx + 1],  # Course Number
                lines[start_idx + 2],  # Course Name
                lines[start_idx + 3],  # Credits
                lines[start_idx + 5],  # End time
                lines[start_idx + 6],  # Lecture days
                lines[start_idx + 4],  # Beginning time
                lines[start_idx + 7],  # Average Grade
                i + 1)                  # Course Numbering
            
            courses.append(course)

        for course in courses: # Print course information
            course.printInfo()
            print()

    except ValueError:
        print("Error: Invalid number format in file.")
