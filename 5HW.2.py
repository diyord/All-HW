class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}, Год выпуска: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def display_info(self):
        super().display_info()
        print(f"Модель: {self.model}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Тип: {self.type}")

car = Car("Toyota", 2022, "Camry")
motorcycle = Motorcycle("Harley-Davidson", 2021, "Chopper")

print("Информация об автомобиле:")
car.display_info()

print("\nИнформация о мотоцикле:")
motorcycle.display_info()