# lets read from csv file this time
'''with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
# another approach
students = []
with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
    print(student)'''

# better sorting
students = []
with open("names.csv") as file:
    for line in file:
        names, house = line.rstrip().split(",")
        student = {"name": names, "house": house}
        students.append(student)
# using lambda function as paramter to sorted function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
