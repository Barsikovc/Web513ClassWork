class Car:
    __wheels = 4

    def __init__(self, brand, color, doors):
        self.brand = brand
        self.color = color
        self.doors = doors

    def drive(self):
        print(f'Автомобиль {self.brand}. Цвет {self.color}. Двери {self.doors} едет!')

    @classmethod
    def describe(cls):  # что для работы с @classmethod вместо self используем cls везде в теле данного метода
        print(f'Легковые автомобили имеют {cls.__wheels} колеса')

    @classmethod
    def change_wheels_quantity(cls, wheels_num):
        Car.check_int_data_type(wheels_num)
        cls.__wheels = wheels_num

    @staticmethod
    # Если не используются атрибуты (класса или экземпляра) используем >> @staticmethod
    # Вызов через self или объект не вызывает ошибку, но это плохой код поэтому вызываем его через класс
    def general_info():
        print(f'Машины это транспортные средства')

    @staticmethod
    def check_int_data_type(data):
        if isinstance(data, int):
            return True
        raise TypeError('Неверный тип данных!')


if __name__ == '__main__':
    car = Car('Toyota', 'красный', 4)
    car.drive()
    Car.describe()
    print()
    Car.change_wheels_quantity(6)
    Car.describe()
    print()
    Car.general_info()

    car.wheels = 4
    # присваиваем новый (неожиданный) атрибут к конкретному объекту
    # (и теперь он отличается от остальных, что может далее вызвать проблемы)
    # не делайте так! Это не меняет значение атрибута класса,
    # если нужно изменить атрибут класса меняйте его через класс (или @classmethod) если он предусмотрен.
    print(car.__dict__)

    car2 = Car('Honda', 'синий', 4)
    print(car2.__dict__)
    Car.change_wheels_quantity(6.5)
