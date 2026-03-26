class Car:
    def __init__(self, brand, color, doors):
        self.brand = brand
        self.color = color
        self.doors = doors

    def drive(self):
        print(f'Автомобиль {self.brand}. Цвет {self.color}. Двери {self.doors} едет!')


if __name__ == '__main__':
    car = Car('Toyota', 'красный', 4)
    car.drive()
