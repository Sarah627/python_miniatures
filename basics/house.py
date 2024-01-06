# last point in conditionals, using match like switch in other languages
name = input("please enter name: ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:  # for who practised another programming languages this is the default case
        print("Who?")
