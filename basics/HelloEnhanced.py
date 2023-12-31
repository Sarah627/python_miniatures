# In this file we are going to deal basically with functions
# The main function here tells this is the main part of the program
# and thus we can list the functions definition underneath it
def main():
    hello()
    name = input("Please enter your name:").strip().title()
    hello(name)
    number = int(input("enter a number you want to format: "))
    print(formatNumber(number))


def hello(name="world!"):
    print(f"Hello, {name}")

# function with a return value
def formatNumber(number):
    return f"{number:,}"


main()
