while True:
    try:
        x = int(input("What's x?: "))
    except ValueError:
        print("X is not an integer, please enter integer")
    else:
        print(f"x is {x}")
        exit()
