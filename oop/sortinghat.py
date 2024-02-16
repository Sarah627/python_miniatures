from random import choice


class Hat:
    # houses is a class variable
    houses = ["Hufflepuff", "Gryffindor", "Ravenclaw", "Slytherin"]

    # equivalent to static methods in java
    @classmethod
    def sort(cls):
        print("your house is: " + choice(cls.houses))
