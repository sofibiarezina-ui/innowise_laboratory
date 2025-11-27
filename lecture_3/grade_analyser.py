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

students = {}
greeting()
choice = int(input())
while choice != 5:
    if choice == 1:
        name = input("Enter student name: ")
        students[name] = []
    elif choice == 2:
        name = input("Enter student name: ")
        entering_grades = True
        while entering_grades:
            try:
                grade = input("Enter a grade (or 'done' to finish): ")
                if grade == 'done':
                    entering_grades = False
                if entering_grades:
                    students[name].append(int(grade))
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == 3:
        print('---Student Report---')
        if students != {}:
            average_grades = []
            for student in students:
                try:
                    average_grades.append(sum(students[student])/len(students[student]))
                    print(f"{student}'s average grade is {average_grades[len(average_grades)-1]}.")
                except ZeroDivisionError:
                    print(f"{student} has no grades.")
            if average_grades != []:
                print("--------------------------")
                print(f"Max Average: {max(average_grades)}.")
                print(f"Min Average: {min(average_grades)}.")
                print(f"Overall Average: {sum(average_grades) / len(average_grades)}.")

        else:
            print("There are no students.")
    greeting()
    choice = int(input())
