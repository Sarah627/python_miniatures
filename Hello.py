# Prompit user for his/her name
# name = input("please enter your name:").strip().title()
name = input("please enter your name: ")
# Remove white space from a string using .strip method
name = name.strip()
# Capitalize user's name but this capitalize the first word only
name = name.capitalize()
# We can capitalize every word using title method, in case for example the user entered his|her first and alst name
# we can do this directly -->  name = name.strip().title() nested method invoking
name = name.title()
# We can split user's name string into substrings using split method as follows:
first_name, last_name = name.split(" ")
# Greet user with his/her name
print("Hello,", name)
# Using print different parameters
print("Thank you", name, end='\t', sep=', ')
print("after this line the print function will be re-adjusted", sep=' ', end='\n')
# Using format string method to print a name from a variable
print(f"See you again, {first_name}!")

# we are using the formal definition of print function
# print(*objects, sep = ' ', end='\n', file=sys.stdout, flush = False)
# just the very first code line in python, printing
# hello, world on the console, we'are just using the print function print()
# if we wanna write text so insert this text in a double quotes
# in the parenthesis of the print function, and that's it!

# to interpret the code in the terminal, type python filename.py
