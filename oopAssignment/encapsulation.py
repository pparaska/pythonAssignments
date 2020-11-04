class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Car(200, 'black')
audi = Car(300, 'red')

ford.__speed = 400
print(ford.get_speed())
print(audi.get_speed())
print(ford.get_color())
print(audi.get_color())
