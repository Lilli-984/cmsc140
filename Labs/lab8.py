# Calculating Grades 

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

student_names = ["Anna",
    "Betsy",
    "Carol",
    "Delilah",
    "Emily",
    "Francesca",
    "Gemini"
    ]

student_grades = [
    [89, 90, 77],
    [58, 77, 80],
    [99, 100, 94],
    [29, 9, 0],
    [100, 88, 92],
    [82, 84, 87],
    [74, 68, 88]
]

# create a dictionary where:
#  the key is the student name
#  the value is the average of the student's three exam scores
students = {}
i=0
for name in student_names:
    
    avg = (sum(student_grades[i]))/len(student_grades[i]) #indexed students_grades so it can return a value instead of a list
    students[name] = avg  #took out quotes around name so its the local variable instead of a string
    i+=1


# create another dictionary where:
#  the key is the student name
#  the value is the student's letter grade 
grades = {}

for student, avg in students.items():
    # this should follow the grading scheme outlined above:
        # 90+	A
        # 80-89	B
        # 70-79	C
        # 60-69	D
        # 0-59	F

    if avg >= 90:
        letter_grade = "A"
    if avg <= 89:           #Added a colon to if statement to fix syntax error
        letter_grade = "B"
    if avg <= 79:
        letter_grade = "C"   #changed single quote to double to fix string syntax
    if avg <= 69: 
        letter_grade = "D"
    if avg <= 59:  #Changed comparisons to accuratly reflect grading scheme and changed else to if to properly compare avg.
        letter_grade = "F"
    grades[student] = letter_grade



for student, grade  in grades.items(): #added .items() to the dictionary so both the key and value can be called 

    print("Student: " + student)

    # print the average exam score 
    print("Exam Average: " , students[student]) #changed avg to student to get the value and the + to a comma.
    # print the letter grade
    print("Grade: "+ grade)  #added a plus sign to fix print function

    if grade is "F":  #corrected letter_grade to grade to call local variable name.
        print(f"{student} is failing.") #added f to string to use f-string
    else:
        print(f"{student} is passing.")  #added f to string to use f-string