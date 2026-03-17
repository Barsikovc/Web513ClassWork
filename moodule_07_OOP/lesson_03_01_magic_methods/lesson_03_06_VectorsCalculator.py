import math


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        raise TypeError("Объекты относятся к разным классам!")

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        raise TypeError("Объекты относятся к разным классам!")

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        raise TypeError("Объекты относятся к разным классам!")

    def __len__(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2))

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def __str__(self):
        return f'Вектор с координатами (x = {self.x}, y = {self.y})'

    def __repr__(self):
        return f'Vector2D({self.x}, {self.y})'


if __name__ == '__main__':
    vector1 = Vector2D(3, 4)
    vector2 = Vector2D(1, 2)
    vector3 = Vector2D(1, 2)

    print(vector1 + vector2)
    print(vector1 - vector2)
    print(vector2 == vector3)
    print(len(vector1))
    print(f'Длина: {vector1.length():.2f}')
    print(f'Угол: {vector2.angle():.2f}')
