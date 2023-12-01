class Account:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName


    def bankBruker(self):
        welcomeMessage = f"Welcome {self.name} {self.lastName}"
        return welcomeMessage

