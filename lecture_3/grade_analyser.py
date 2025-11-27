#the beginning of every request
def greeting():
    print('''
    ---Student Grade Analyser---
    1. Add a new student
    2. Add grades for a student
    3. Generate a full report
    4. Find the top student
    5. Exit
    ''')
    print("Enter your choice: ", end="")

def choose(): #check if the input for a choice is valid
    entering_choice = True
    while entering_choice:
        try:
            choice = int(input())
            entering_choice = False
        except ValueError:
            print("Invalid input. Please enter a number.")
            print("Enter your choice: ", end="")
    return choice

students = {}
greeting()
choice = choose()
#check if the user wants to exit the program
while choice != 5:
    #function of the first choice
    if choice == 1:
        name = input("Enter student name: ")
        students[name] = []  #create an empty list to fill it with marks
    #function of the second choice
    elif choice == 2:
        entering_name = True
        while entering_name:
            try:
                name = input("Enter student name: ")
                a = students[name]
                entering_name = False
            except KeyError:
                print("There is no student in list with such name. Please enter a student name.")
        entering_grades = True  #flag to understand if the user wants to add more new marks
        while entering_grades:
            try:  #check if the input is int or "done"
                grade = input("Enter a grade (or 'done' to finish): ")
                if grade == 'done':
                    entering_grades = False  #user don't want to add new marks
                if entering_grades:
                    students[name].append(int(grade))
            except ValueError:
                print("Invalid input. Please enter a number.")
    #the function of the third choice
    elif choice == 3:
        print('---Student Report---')
        if students != {}:  #check if there are any students
            average_grades = []
            for student in students:
                try:  #except the situation as ZeroDivision
                    average_grades.append(sum(students[student])/len(students[student]))  #calculate the average grade
                    print(f"{student}'s average grade is {average_grades[len(average_grades)-1]}.")
                except ZeroDivisionError:
                    print(f"{student}'s average grade is N/A.")
            if average_grades != []: #check if anybody has grades to sum up
                print("--------------------------")
                print(f"Max Average: {max(average_grades)}.")
                print(f"Min Average: {min(average_grades)}.")
                print(f"Overall Average: {sum(average_grades) / len(average_grades)}.")
        else:
            print("There are no students.")
    #the function of fourth choice
    elif choice == 4:
        if students != {}: #check if there are any students
            average_grades = {}  # create a dictionary to save name of the student and his average grade
            for student in students:
                if students[student] != []:
                    average_grades[student] = (sum(students[student])/len(students[student]))
            if average_grades != {}:
                best_student = max(average_grades, key=average_grades.get)
                print(f"The student with the highest average grade is "
                      f"{best_student}"
                      f" with the grade of {average_grades[best_student]}.")
    else:
        print("Invalid input. Please enter a valid choice.")
    greeting()
    choice = choose()
print('Exiting program.')
