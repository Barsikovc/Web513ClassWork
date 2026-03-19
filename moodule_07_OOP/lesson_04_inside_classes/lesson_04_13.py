"""
Композиция
"""


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def __str__(self):
        return f'Тип двигателя: {self.engine_type}'


class Doors:
    def __init__(self, doors_quantity, engine):
        self.doors_quantity = doors_quantity
        self.engine = engine

    def __str__(self):
        return f'Количество дверей: {self.doors_quantity}'


class Wheels:
    def __init__(self, radius, doors):
        self.radius = radius
        self.doors = doors

    def __str__(self):
        return f'Радиус диска: {self.radius}'


class Car:
    def __init__(self, wheels):
        self.wheels = wheels

    def display_info(self):
        print('Автомобиль:')
        print(self.wheels)
        print(self.wheels.doors)
        print(self.wheels.doors.engine)


if __name__ == '__main__':
    car = Car(Wheels('17', Doors('4', Engine('ДВС'))))
    car.display_info()
