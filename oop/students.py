class Student:
    # applying abstraction and encapsulation
    def __init__(self, name, house, patronus=None):
        self.name = name  # attributes
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} and your patronus is {self.charm()}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🍕"
            case "Otter":
                return "🍰"
            case "Doe":
                return "\nLily, After all this time? "
            case  _:
                return "🌿"
    # Getter and Setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    # Getter
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Syltherin", "Hafflbuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    # student.house = "Number Four, Privet Drive "
    print(student)


def get_student():
    name = input("What's your name? ")
    house = input("What's your house? ")
    patronus = input("Enter your Patronus: ")
    try:
        return Student(name, house, patronus)
    except ValueError:
        pass


if __name__ == "__main__":
    main()
