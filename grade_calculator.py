"""
Student Grade Calculator

This program calculates student averages, assigns letter grades,
finds the top performer, and calculates class statistics.
"""


# Dictionary containing student names and their grades.
student_grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [75, 80, 82]
}


# Dictionary to store each student's average.
student_averages = {}


# Calculate the average for each student.
for student_name, grade_list in student_grades.items():
    average_score = sum(grade_list) / len(grade_list)
    student_averages[student_name] = average_score


# Dictionary to store each student's letter grade.
student_letter_grades = {}


# Assign a letter grade using the grading scale.
for student_name, average_score in student_averages.items():

    if average_score >= 90:
        letter_grade = "A"
    elif average_score >= 80:
        letter_grade = "B"
    elif average_score >= 70:
        letter_grade = "C"
    elif average_score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    student_letter_grades[student_name] = letter_grade


# Find the student with the highest average.
top_student = ""
top_average = -1

for student_name, average_score in student_averages.items():

    if average_score > top_average:
        top_average = average_score
        top_student = student_name


# Calculate the overall class average.
total_average = 0

for average_score in student_averages.values():
    total_average += average_score

class_average = total_average / len(student_averages)


# Count students who received a passing grade (C or better).
passing_students = 0

for letter_grade in student_letter_grades.values():

    if letter_grade in ["A", "B", "C"]:
        passing_students += 1


# Display the results.
print("========================================")
print("       STUDENT GRADE CALCULATOR")
print("========================================")

print("\nStudent Results:")
print("----------------------------------------")

for student_name in student_grades:
    print(
        f"{student_name}: "
        f"Average = {student_averages[student_name]:.2f}, "
        f"Letter Grade = {student_letter_grades[student_name]}"
    )

print("\nTop Performer:")
print("----------------------------------------")
print(f"Student: {top_student}")
print(f"Average Grade: {top_average:.2f}")

print("\nClass Statistics:")
print("----------------------------------------")
print(f"Overall Class Average: {class_average:.2f}")
print(f"Number of Students Who Passed: {passing_students}")

print("\n========================================")
print("             PROGRAM COMPLETE")
print("========================================")