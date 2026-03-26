class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # надо сравнивать все ЗНАЧИМЫЕ атрибуты объекта!
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.age == other.age
        else:
            raise TypeError('Объекты относятся к разным классам!')


if __name__ == '__main__':
    s1 = Student('Иван', 16)
    s2 = Student('Иван', 16)
    s3 = Student('Мария', 15)
    print(s1 == s2)
    print(s1 == s3)
