# we'll going to use modulo operator '%'
# implementing how to answer the question if this number is even or odd
def main():
    x = int(input("enter a number to check:"))
    if is_even(x):  # change is even to other functions defined beneath :))
        print("even value")
    else:
        print("odd")


def is_even(number):
    if number % 2 == 0:
        return True  # returning boolean value
    else:
        return False

# let's do something pythonic


def check_even(num):
    return True if num % 2 == 0 else False


def even_or_odd(n):
    return n % 2 == 0


main()
