class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad
    
    def get_edad (self):
        return self.__edad
    def set_edad (self,nueva_edad):
        if nueva_edad > 0:
            self.__edad +=nueva_edad

Persona1 = Persona("Luis", 18)

print(Persona1.nombre, Persona1.get_edad())
Persona1.set_edad(2)
print(Persona1.nombre, Persona1.get_edad())





    

    