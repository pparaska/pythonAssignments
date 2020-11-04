from builtins import print
from msilib import CAB


class Car:
    def __init__(self, color, speed):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed(value)

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color(value)

    def get_color(self):
        return self.__color

    ford


ford = Car('red', 100)
audi = Car('black',120)
print(ford.get_speed())
print(ford.get_color())

# ford.speed = 22
# ford.color = 'black'
# audi.speed = 30
# audi.color = 'red'

