# more practicing on loops concept, let's build mario world
# the hash symbol '#' for columns and question mark '?' for rows
def main():
    print_column(3)
    print_row(4)
    print_2dworld(5)
    twoD_world(10)


def print_row(width):
    print("?" * width)


def print_column(height):
    for _ in range(height):
        print("#")

# The use of nested loops


def print_2dworld(size):
    # for building column
    for i in range(size):
        # for building row
        for j in range(size):
            # unit brick
            print("#", end=" ")
        print()


# another simple solution to the same problem
print()


def twoD_world(size):
    for _ in range(size):
        print("# " * size)


main()
