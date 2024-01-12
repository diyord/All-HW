class Animal:
    def make_sound(self):
        pass  # Абстрактный метод

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу-мяу!"

class Cow(Animal):
    def make_sound(self):
        return "Му-му!"

dog = Dog()
cat = Cat()
cow = Cow()

print("Собака говорит:", dog.make_sound())
print("Кошка говорит:", cat.make_sound())
print("Корова говорит:", cow.make_sound())