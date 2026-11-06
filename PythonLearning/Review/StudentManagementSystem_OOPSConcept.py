counter = 0
class Student:
#   name , studentID , marks[]
    def __init__(self, name, grade, email):
        global counter
        counter = counter +1
        self.student_ID = counter  #get from the configuration file to generate the latest student ID
        self.student_name = name
        self.student_grade = grade
        self.student_email = email
        self.student_courses = []
        self.student_marks = []
        self.average = 0

    def enroll_courses(self, course_name):
        self.student_courses.extend(course_name)


    def enter_marks(self):
        for i in range(len(self.student_courses)):
            self.student_marks.append(int(f"Enter the marks {self.student_courses[i]}: "))

    def display_info(self):
        print("Student details: ")
        print(f'Student ID: {self.student_ID}')
        print(f'Student Name: {self.student_name}')
        print(f'Student Grade: {self.student_grade}')
        print(f'Student Email: {self.student_email}')
        print(f'Student Courses: ')
        if not self.student_courses:
            print("No enrolled courses.")
        else:
            for i in self.student_courses:
                print(i)


    def get_grade(average):
        result = ""
        if average >= 90:
            result = "A"
        elif average >= 80:
            result = "B"
        elif average >= 70:
            result = "C"
        elif average >= 60:
            result = "D"
        else:
            result = "F"
        return result


if __name__ == '__main__':
    student1 = Student("Shravya", "9", "shravyi.ak@gmail.com")
    student2 = Student("Sky", "9", "skyott1117@gmail.com")
    student3 = Student("Aarnavi", "9", "aarnavi.jain0220@gmail.com")
    student1.display_info()
    student2.display_info()
    student1.enroll_courses(["Spanish", "Algebra2/Trig", "Biology", "Literature"])
    student1.display_info()
    student1.enter_marks()
