import csv
students = []
with open("names.csv") as file:
    reader = csv.reader(file)  # list is returned
    for name, house in reader:
        students.append({"name": name, "house": house})
# using lambda function as paramter to sorted function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
