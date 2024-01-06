x = int(input("please enter any numerical value:"))
y = int(input("please enter another numerical value:"))
if x < y:
    print("the second number is greater than the first number")
if x > y:
    print("the first number is greater than the second number")
if x == y:
    print("both numbers are equal")

# we can make an enhancement using elif and else:
if x < y:
    print("y is greater than x")
elif x > y:
    print("x is greater than y")
else:
    print("they are equal")
# we use them for reducing complexity of the program
# let's use some logic operators and change the game
if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")
# one more time
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
