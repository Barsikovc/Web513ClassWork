"""
Агрегация
"""


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def __str__(self):
        return f'Тип двигателя: {self.engine_type}'


class Doors:
    def __init__(self, doors_quantity):
        self.doors_quantity = doors_quantity

    def __str__(self):
        return f'Количество дверей: {self.doors_quantity}'


class Wheels:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Радиус диска: {self.radius}'


class Car:
    def __init__(self, wheels, doors, engine):
        self.wheels = wheels
        self.doors = doors
        self.engine = engine

    def display_info(self):
        print('Автомобиль:')
        print(self.wheels)
        print(self.doors)
        print(self.engine)


if __name__ == '__main__':
    engine = Engine('ДВС')
    doors = Doors(4)
    wheels = Wheels(17)
    car = Car(wheels, doors, engine)
    car.display_info()
