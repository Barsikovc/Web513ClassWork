"""
Агрегация
"""


class Body:
    def __init__(self, body_type):
        self.body_type = body_type

    def display(self):
        print(f'Материал корпуса: {self.body_type}')

    def check(self):
        return f'Корпус из: {self.body_type} проверен'


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display(self):
        print(f'Тип двигателя: {self.engine_type}')

    def check(self):
        return f'Двигатель типа: {self.engine_type} проверен'


class Wheels:
    def __init__(self, wheels_type):
        self.wheels_type = wheels_type

    def display(self):
        print(f'Тип двигателя: {self.wheels_type}')

    def check(self):
        return f'Шасси типа: {self.wheels_type} проверены'


class Plane:
    def __init__(self, body: Body, engine: Engine, wheels: Wheels):
        self.body = body
        self.engine = engine
        self.wheels = wheels
        self.parts = [self.body, self.engine, self.wheels]

    def display_parts(self):
        for part in self.parts:
            part.display()

    def check_parts(self):
        for part in self.parts:
            print(part.check())


if __name__ == '__main__':
    plane_body = Body('Пластик')
    plane_engine = Engine('Электро')
    plane_wheels = Wheels('Резиновые')

    plane = Plane(plane_body, plane_engine, plane_wheels)
    plane.display_parts()
    plane.check_parts()


