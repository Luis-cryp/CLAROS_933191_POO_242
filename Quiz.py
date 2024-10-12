# class bank_account:
#     def __init__(self, holder):
#         self. holder = holder
#         self. __balance = 0

#     def depositar(self,cantidad):
#         self.__balance+=cantidad

#     def retirar(self,cantidad):
#         if cantidad <= self.__balance:
#             self.__balance -= cantidad

#     def Mostrar(self):
#         return f"El titular de la cuenta{self.holder} tiene un total de{self.__balance}"

# holder = bank_account("David")
# holder.depositar (1000)
# print(holder.Mostrar())
# holder.retirar (500)
# print(holder.Mostrar())

class Carro:
    def __init__(self,marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"Carro: {self.marca},{self.modelo}, Año: {self.año}"

    def __repr__(self):
        return f"Carro(marca='{self.marca}', modelo='{self.modelo}', año={self.año})"

carro_1 = Carro("Toyota", "Corolla", 2022)

print(carro_1)
print(repr(carro_1))
    
    
   