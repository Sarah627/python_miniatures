from sys import argv, exit

if len(argv) < 2:
    exit("Too few arguments")
# using slicing concept
for arg in argv[1:]:
    print("Hello, My name is:", arg)
