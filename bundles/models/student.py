from models.person import Person

class Student(Person):
    def __init__(self, name, age, lastname, code):
        super().__init__(name, age,lastname)
        self.code = code

    def __repr__(self):
        return f"Student(name = {self.name}, lastaname={self.lastname}, age = {self.age}, code = {self.code})"

    def sayHello(self):
        return f"Hola soy un estudiante y me llamo {self.name}"