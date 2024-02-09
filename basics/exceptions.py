while True:
    try:
        x = int(input("What's x?: "))
        break
    except ValueError:
        print("X is not an integer, please enter integer")
