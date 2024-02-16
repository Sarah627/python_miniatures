from wizard import Wizard


class Student(Wizard):
    # applying abstraction and encapsulation
    def __init__(self, name, house, patronus):
        super().__init__(name)
        if house not in ["Gryffindor", "Syltherin", "Hafflbuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} and your patronus:  {self.charm()}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Doe":
                return "\nLily🌺, After all this time? "
            case _:
                return "🐍"

    @classmethod
    def get_student(cls):
        name = input("What's your name? ")
        house = input("What's your house? ")
        patronus = input("What's your patronus? ")
        return cls(name, house, patronus)

    # Getter and Setter
'''    @property
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
        self._house = house'''
