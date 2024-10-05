class car:
    def __init__(self, brand, model, year, price):
        self.__brand = brand 
        self.__model = model
        self.__year = year
        self.__price = price 

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year
    
    def get_price(price):
        return self.__price

    def set_price(self, price):
        self.__price = price
    
    
    #Metodos

    def apply_descount():
        pass 
    
    def __repr__(self):
        return f"marca={self.get_brand()}, modelo={self.get_model()}, año={self.get_year}, precio={self.get_price}"

