# DRY principle, loops with while
# very simple iteration with while, i is smth called counter
# simple program about printing animals voice' clearly for a cat
def main():
    i = 0
    while i < 3:
        print("meow")
        i += 1  # incrementing i 'counter' ,remember '=' is assignment operator, assigns from right to left

    for i in [0, 1, 2]:
        print("meow")

    for _ in range(100):  # using built-in function instead of list
        print("squeek")

    print("meow\n" * 3, end="")

    # when you want the user to enter a certain input we can use the following logic
    # Sentinel control loops which means we don't know how many times this loop will iterate because it depends on user input
    while True:
        number = int(input("what's n?"))
        if number <= 0:
            continue  # loop one more time
        else:
            print("meow\n"*number, end="")
            break  # exit the loop

# solving same problem using different approach
    num = get_number()
    meow(num)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    print("meow\n" * n, end="")


main()
