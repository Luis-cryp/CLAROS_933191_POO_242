# class Person:
#     def __init__(self, name, lastname, age,):
#         self.name =  name
#         self.lastname = lastname
#         self.age = age
#         self.isMarriedWith = None
#         self.nationality = None

    
#     def __repr__(self):
#         return f"Person(name={self.name}, lastname={self.lastname}, age={self.age}, spouse={self.isMarriedWith} nationality={self.nationality})"

#     def __str__(self):
#         return f"name={self.name}, spose={self.isMarriedWith.name}"

#     def get_married(self, person: "person"):
#             self.isMarriedWith = person
#             person.isMarriedWith = self

# person_1 = Person(name="James", lastname="Rodriguez", age="33")
# person_2 = Person(name="Luis", lastname= "Diaz", age=25)
# person_3 = Person(name="Luisa", lastname= "Perez", age=24)

# person_1.get_married(person_3)
# person_3.get_married(person_1)


# print(person_1)
# print(person_3)

class Person:
    def __init__(self, name, lastname, age):
        self.__name = name 
        self.__lastname = lastname
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
        
    
    def __repr__(self):
        return f"name={self.get_name()}, lastname={self.get_lastname()}, age={self.__age}"

person_1 = Person(name="James", lastname="Rodriguez", age=33)
person_2 = Person(name="Luis", lastname= "Diaz", age=25)
person_3 = Person(name="Luisa", lastname= "Perez", age=24)

person_1.set_age(20)

print(person_1)