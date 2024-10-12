#CLASE ABSTRACTA
class Person:
    def __init__(self, dni, name, lastname, age):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.age = age

class Student(Person):
    def __init__(self, dni, name, lastname, age, code):
        super().__init__(dni, name, lastname, age)
        self.code = code
        self.__subjects = []

    def addsubject(self, subject):
        self.__subjects.append(subject)

    def __str__(self):
        return f"Nombre: {self.name}, Codigo: {self.code}, Asignaturas: {self.__subjects}"

class  Professor(Person):
    def __init__(self, dni, name, lastname, age, device, desktop):
        super().__init__(dni, name, lastname, age)
        self.device = device
        self.desktop = desktop

    def __str__(self):
        return f"Nombre: {self.name}, Dispositivo: {self.device}, Puesto de trabajo: {self.desktop}"


student_1 = Student(1234,"Luis", "Soto", 21, 12233)
professor_1 = Professor(1234,"Luis", "Soto", 31, "Laptop", 16)

   
student_1.addsubject ("Matematicas")

print(student_1)
print(professor_1)