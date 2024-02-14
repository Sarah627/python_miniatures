# file = open("names.txt", "a")  # returns a file handle

# for _ in range(3):
#     name = input("What's your name? ")
#     file.write(f"{name} ")
# file.close()

# name = input("What's your name? ")

# use another approach to automatically close the file
'''with open("names.txt", "a") as file:
    file.write(f"{name} ")

with open("names.txt", "r"):
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip())'''

# reading first, sorting then print them all sorted

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):  # , reverse=True as an argument to sorted
    print(f"Hello, {name}")
