# let's learn how to deal with a list and applying using loops in the same time
students = ["Harry", "Hermione", "Ron"]
for student in students:
    print(student)  # we can use underscore but it would be less readable
"""
what happened?
the iteration variable student will be assigned
to the value of each element in the list 

"""
# here we are using the len function which returns the length of the list since range function takes only integer values as inputs

for i in range(len(students)):
    # what's between the square brackets is called the index, starts from 0
    print(i + 1, students[i])

# using another data type dictionary 'dict' for associating key with a value
# let's ask the question of Who is in what house? let's solve the problem
# notice the curly braces
std = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in std:
    print(student, std[student], sep=", ")

# let's make it more complicated, let's use a list of dictionaries
s = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
    {
        "name": "Severus Sanpe",
        "house": "Slytherin",
        "patronus": "doe -after all this time?-",
    },
]
for person in s:
    print(person["name"], person["house"], person["patronus"], sep=", ")
