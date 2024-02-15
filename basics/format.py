# This is a simple program for formatting your name
from re import search
name = input("What's your name?").strip()
# We are supposing that you enter your last name first separated with a comma then your first name
if "," in name:
    last, first = name.split(",")
    name = f"{first} {last}"
print(f"Hello, {name}")

# Implementing the same idea using different approach

Name = input("What's your name? ").strip()
if matches := search(r"^(\w+), ?(\w+)$", Name):
    Name = matches.group(2)+" "+matches.group(1)
print(f"Hello, {Name}")
