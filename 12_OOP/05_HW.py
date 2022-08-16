from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def desc(self):
        pass

    @abstractmethod
    def licence(self):
        pass

class Bike(Vehicle):
    def licence(self):
        return "AM"

    def desc(self):
        return "You can pass your bike card in age: 10+"

class Car(Vehicle):
    def licence(self):
        return "B"

    def desc(self):
        return "You can pass your car licence at age 18+"

    def max_speed(self):
        return "100"


class Truck(Vehicle):
    def licence(self):
        return "C"

    def desc(self):
        return "Bigger Car"


class Bus(Vehicle):
    def licence(self):
        return "E"

    def desc(self):
        return "You can transport people"


if __name__ == "__main__":
    b= Bike()
    print(b.desc())
    print(b.licence())