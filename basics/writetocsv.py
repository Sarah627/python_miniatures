import csv

name = input("What's your name? ")
house = input("What's your house? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])
