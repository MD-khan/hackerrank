#!/usr/bin/env python3
"""
Given the names and grades for each student in a class of  
students, store them in a nested list and print the name(s) 
of any student(s) having the second lowest grade
"""

# import re


# students = []
# n_of_student = input(f"Enter the total student: ")

# for _ in range(int(n_of_student)):
#     studen_name = input(f"Enter Student Name: ")
#     student_score = float(input(f"Enter the Score: "))
#     # name.append(studen_name)
#     # score.append(student_score)
#     students.append([studen_name, student_score])

# students = [['Harry', 37.21], ['Berry', 37.21], [
#     'Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

students = [['Harry', 30.0], ['Berry', 30.0], [
    'Tina', 31.0], ['Akriti', 41.0], ['Harsh', 39.0]]
students.sort()
#print(min(students, key=lambda x: x[1]))

# find the lowest grade
lowest_grade = min(students, key=lambda x: x[1])
l_g_s = []
for student in students:
    if lowest_grade[1] == student[1]:
        l_g_s.append(student)

new_student_list = []
for student in students:
    if student not in l_g_s:
        new_student_list.append(student)
#print(new_student_list)

# Now find again the min score
# This score is the second lowest score
# Because the min score/scores removed

second_lowest_grade = min(new_student_list, key=lambda x: x[1])


# find the same result if any of student have
result = []
for student in new_student_list:
    if second_lowest_grade[1] == student[1]:
        result.append(student)

for r in result:
    print(r[0])


# # find again the lowest grade value
