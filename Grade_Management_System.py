grades = {
    "english": [90, 95, 81],
    "math": [100, 95, 92, 98],
    "history": [76, 98]
}
chosenSubject = ""

def reportingMaintenanceMenu():
    print("\n*************************\nReporting and Maintenance\n")
    print("1 - Reporting\n2 - Maintenance\n0 - Exit")
    functionChoice = input("\nWhich function: ")
    if functionChoice == "0":
        mainMenu()
    elif functionChoice == "1":
        reportingMenu()
    elif functionChoice == "2":
        maintenanceMenu()
    else:
        print("\nNot a valid function, please try again...")
        reportingMaintenanceMenu()

def reportingMenu():
    marks = grades[chosenSubject]
    print("********************\nGrade Reporting")
    reportingChoice = input("Commands: best, worst, average, end, summary: ")
    if reportingChoice == "best":
        best = max(marks)
        print(f"Your best score in {chosenSubject} was: {best}")
        reportingMenu()
    elif reportingChoice == "worst":
        worst = min(marks)
        print(f"Your worst score in {chosenSubject} was: {worst}")
        reportingMenu()
    elif reportingChoice == "average":
        avg = sum(marks)/len(marks)
        print(f"Your average score in {chosenSubject} was: {avg}")
        reportingMenu()
    elif reportingChoice == "end":
        reportingMaintenanceMenu()
    elif reportingChoice == "summary":
        print(f"Currently the grades are: {marks}\n")
        reportingMenu()
    else:
        print("\nNot a valid choice, please try again...")
        reportingMenu()

def maintenanceMenu():
    print("\n****************************\nMaintaining Grades for " + chosenSubject)
    print("Currently the grades are: " + str(grades[chosenSubject]))
    maintenanceChoice = input("1 - Change a Grade\n2 - Add a Grade\n3 - Delete a Grade\n4 - End\nWhat would you like to do: ")
    if maintenanceChoice == "1":
        gradeToChange = input("Which grade should be changed: ")
        if int(gradeToChange) not in grades[chosenSubject]:
            print(f"That is not a grade in {chosenSubject}")
            maintenanceMenu()
        else:
            newGrade = input("What is the new grade : ")
            grades[chosenSubject].remove(int(gradeToChange))
            grades[chosenSubject].append(int(newGrade))
            maintenanceMenu()
    elif maintenanceChoice == "2":
        newAdd = input("What is the new grade: ")
        grades[chosenSubject].append(int(newAdd))
        print(f"Ok, {chosenSubject} now has the following grades: {grades[chosenSubject]}")
        maintenanceMenu()
    elif maintenanceChoice == "3":
        newDeletion = input("What is the grade to delete: ")
        grades[chosenSubject].remove(int(newDeletion))
        print(f"Ok, {chosenSubject} now has the following grades: {grades[chosenSubject]}")
        maintenanceMenu()
    elif maintenanceChoice == "4":
        reportingMaintenanceMenu()
    else:
        print("\nNot a valid choice, please try again...")
        maintenanceMenu()

def mainMenu():
    print("\n*********\nMain Menu\n")
    print("Your grade manager contains grades for: \n")
    for x in list(grades.keys()):
        print(" > " + x, sep="\n")
    classChoice = input("\nWhich class would you like to work with or type 'end' to finish (" + ", ".join(list(grades.keys())) + "): ")
    if classChoice == "end":
        exit(0)
    if classChoice not in grades.keys():
        print("Class does not exist, please try again...")
        mainMenu()
    else:
        global chosenSubject
        chosenSubject = classChoice
        reportingMaintenanceMenu()

print('''
--------------------------------
    Grade Management System
--------------------------------''')
mainMenu()