#Initializes grade, which will update throughout the program
current_grade = 0]
#Gets number of labs from user, verifies the number and adds it to the grade
while True:
    try:
        number_labs = int(input("Enter the number of labs completed: "))
        if number_labs < 6 and number_labs >= 0:
            current_grade = number_labs / 6 * 20
            break
        elif number_labs > 0:
            current_grade = 20
            break
    except (ValueError):
        print("Enter a number")

#Gets number of quizzes from user, verifies the number and adds it to the grade
while True:
    try:
        number_quiz = int(input("Enter the number of quizzes completed: "))
        if number_quiz <= 6 and number_quiz >= 0:
            current_grade += number_quiz/6 * 15
            break
        elif number_labs > 0:
            current_grade += 15
            break
    except (ValueError):
        print("Enter a number")

list_lab = []
list_quiz = []
list_assign = []
list_midterm = []

#Loops through assignments to get number
for i in range(4):
    while True:
        try:
            temp_grade = int(input(f"Enter grade for Assignment {i + 1}: "))
            if temp_grade > 100 or temp_grade < 0:
                print("Enter a valid grade")
            else:
                list_assign.append(temp_grade)
                break
        except (ValueError):
            print("Enter a number")
for i in range(2):
    while True:
        try:
            temp_grade

            
