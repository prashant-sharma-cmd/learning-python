def report_card(local_roll,local_student):
    output = f"""
{local_student["name"]}'s Report Card

Name: {local_student["name"]}
Roll number: {local_roll}

<--Marks in various subjects -->          
"""
    print(output)
    for local_subject in subjects:
        print(f"{local_subject}: {local_student['marks'][local_subject]}")

    print(
        f"TOTAL MARKS: {local_student['total']} \nPercentage: {local_student['percentage']}%")

print(" Welcome to Student Report Card Management System")
data = {}
subjects = ["Physics", "English", "Maths", "Chemistry", "Computer"]

while True:
    print("What do you want to do?")
    task = input("Add -> Add new student data \nView -> View all student data\n"
                 "Topper -> Display the class topper \nSearch -> Search student by roll no.\n"
                 "Failures -> Display the data of failed students\n"
                 "Update -> Update student marks\n"
                 "Exit -> Exit program\n")

    if task == "Add":
        name = input("Enter student name: ")
        roll_no = input("Enter student roll no: ")
        marks = {}
        for subject in subjects:
            mark = int(input(f"Enter student's marks in {subject}: "))
            marks[subject] = mark
        total = sum(marks.values())
        percentage =  total / len(subjects)
        data[roll_no] = {"name": name, "marks": marks, "total":total,"percentage": percentage}

    elif task == "View":
        for roll_no, student in data.items():
            report_card(roll_no, student)

    elif task == "Topper":
        topper = []
        highest = max([student['total'] for student in data.values()])
        for student in data.values():
            if student['total'] == highest:
                topper.append(student['name'])
        print("The list of topper(s) is:")
        for item in topper:
            print(item)

    elif task == "Search":
        roll = input("Enter the student's roll number: ")
        report_card(roll, data[roll])

    elif task == "Failures":
        failures = []
        for student in data.values():
            for mark in student["marks"].values():
                if mark < 40:
                    failures.append(student["name"])
                    break
        print("The list of failures is:")
        for item in failures:
            print(item)


    elif task == "Update":
        change = input("Enter the student's roll number and subject to update: ")
        roll, subject = change.split(" ")
        new_marks = int(input("Enter the new mark: "))
        data[roll]['marks'][subject] = new_marks
        print("Updated successfully!!")

    elif task == "Exit":
        break









