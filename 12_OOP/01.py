class Animal:
    def show_feature(self):
        return "Są cudzożywne"

class Mammal(Animal):
    def is_lifeborn(self):
        return True

class Dog(Mammal):
    def __init__(self, race):
        self.race = race

piesio = Dog("Kundel")
print(piesio.race)
print(piesio.show_feature())