class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    def define_wiz(self):
        print(f"Hello, Wizard {self.name} has entered the game!")
