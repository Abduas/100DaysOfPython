# Input a Python list of student heights
print("enter a list of student heights ")
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆1
  
# Write your code below this row 👇
student_height=0
for height in student_heights:
  student_height+=height
print(f"total height = {student_height}")

no_of_students=0
for students in student_heights:
  no_of_students+=1
print(f"number of students = {no_of_students}")

average_height=round(student_height/no_of_students)
print(f"average height = {average_height}")