class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # оба этих метода всегда должны ВОЗВРАЩАТЬ строку!
    # __repr__ должен возвращать строку, согласно которой мы можем создать аналогичный объект
    def __str__(self):
        return f'Имя студента: {self.name}, возраст студента: {self.age}'

    def __repr__(self):
        return f'Student("{self.name}", {self.age})'


if __name__ == '__main__':
    student = Student('Иван', 25)
    print(student)
    print(repr(student))
    print(student.__repr__())
