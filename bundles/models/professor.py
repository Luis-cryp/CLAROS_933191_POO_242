from models.person import Person

class Professor(Person):
    def __init__(self, name, lastname, age, bachelor =True):
        super().__init__(name, lastname, age)
        

    def __repr__(self):
        return f"Professor(name = {self.name}, lastname = {self.lastname})"

    def sayHello(self):
        return f"Hola soy un profesor y mi nombre es: {self.name}"