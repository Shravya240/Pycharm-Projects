'''Question 2 - Student Grade Management System
10 Points
Create a program that manages the grades of a class.
The program should first ask:
How many students?
For each student, ask for:
Student name
3 test scores
Requirements
Your program must:
Store the student information using lists.
Calculate each student's average.
Determine the letter grade:
90+  → A
80–89 → B
70–79 → C
60–69 → D
Below 60 → F
Display a report similar to:
===== CLASS REPORT =====
Name: Alex
Average: 87.3
Grade: B
Name: Sarah
Average: 94.0
Grade: A
At the end, display:
Class average
Highest average
Lowest average
Name of the student with the highest average
Requirements:
You must use at least one function.
You must use a loop.
Scores must be between 0 and 100.'''

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

students = []
averages = []
grades = []

num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter student name: ")
    score1 = float(input("Enter test score #1: "))
    score2 = float(input("Enter test score #2: "))
    score3 = float(input("Enter test score #3: "))

    average = (score1 + score2 + score3) / 3
    average = round(average, 1)
    grade = get_grade(average)
    students.append(name)
    averages.append(average)
    grades.append(grade)

print("==== CLASS REPORT ====")
for i in range(num_students):
    print("Name: ", students[i])
    print("Average: ", averages[i])
    print("Grade: ", grades[i])

class_average = sum(averages)/ num_students
highest = max(averages)
lowest = min(averages)
position = averages.index(highest)

print("Class Average: ", class_average)
print("Highest Average: ", highest)
print("Lowest Average: ", lowest)
print("Student with highest average: ", students[position])
