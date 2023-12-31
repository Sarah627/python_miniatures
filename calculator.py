# In this file we're going to do some python code using integers
# Be careful! input function treat its inputs as strings, so
# we're going to use casting
x = input("enter the first number:")
y = input("enter the second number:")
sum = int(x) + int(y)
# Boom! very simple summation calculator
print(sum)
# We acn perform casting like following
print("The subtraction operation")
# note the function nesting we're doing direclty to cast string into int
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print(f"the result is {a-b}")
# We can also write this all down in one single line
print("The multiplication operation")
# Note: in the terminal enter the first number then enter second number
print(int(input()) * int(input()))
# But it's not recommended since it makes the code ugly and hard
# to understand sometimes, if we assumed that the line could be longer
# Remember the goal always to make the code readable

# That's enough for integers, switching to floats
print("let's play with floating point")
divident = float(input("please enter the divident"))
divisor = float(input("please enter the divisor"))
result = divident/divisor
print(result)
# Let's try rounding
# do this first because if you rounded to the nearst integer the number will be an integer, you cannot round it to the nearst two numbers after the floating point
result = round(result, 2)
print(f"rounded result - 2 numbers after the floating point-: {result}")
# We can do the same thing using format string
res = 45.33343452
print(f"{res:.2f}")
result = round(result)
print(f"rounded result -to the nearst integer-: {result}")
# how to use seperators in large numbers? formatted text :-D
number = int(input("enter any number larger than 999"))
print(f"{number:,}")
