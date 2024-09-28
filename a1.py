#Initializes users grade, will update with every received grade
current_grade = 0

#Def function to update grade, takes a score and a weight and updates it to the grade
def update_grade(score, weight):
    global current_grade
    current_grade += + score * weight

number_labs = int(input("Enter the number of labs completed: "))
if number_labs > 6:
    number_labs = 6
update_grade(number_labs/6, 20)


number_quizzes = int(input("Enter the number of quizzes completed: "))
if number_quizzes > 6:
    number_quizzes = 6
update_grade(number_quizzes/6, 15)

for i in range(4):
    assignment_grade = int(input(f"Enter grade for Assignment {i + 1}: "))
    update_grade(assignment_grade/100, 4)

for i in range(2):
    midterm_grade = int(input(f"Enter garde for Midterm {i + 1}: "))
    update_grade(midterm_grade/100, 25/2)

final_grade = int(input("Enter grade for Final Exam: "))
update_grade(final_grade/100, 18)

prep_grade = int(input("Enter grade for Midterm and Final Preperation: "))
update_grade(prep_grade/100, 6)

#Rounds and prints final grade for user
print(f"Your grade is: {int(current_grade)}")

            
