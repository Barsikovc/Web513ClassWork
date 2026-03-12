class Student:
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.marks = {}

    def get_a_mark(self, mark, discipline):
        self.marks[discipline] = mark
        print(f'{self.name} {self.surname} получил оценку {mark} по курсу {self.course}, дисциплина {discipline}.')

    def display_student_marks(self):
        print(f'Студент: {self.name} {self.surname}.\nКурс: {self.course}')
        for discipline, mark in self.marks.items():
            print(f'Дисциплина: {discipline} >> {mark}')


if __name__ == '__main__':
    students = [
        ['Иван', 'Иванов', 'Python'],
        ['Петр', 'Петров', 'QA'],
    ]
    students_objects = []
    for name, surname, course in students:
        students_objects.append(Student(name, surname, course))

    student1, student2 = students_objects
    student1.get_a_mark(8, 'Строки')
    student1.get_a_mark(9, 'Списки')
    student1.get_a_mark(7, 'Словари')
    student1.display_student_marks()
    print(student1.marks)
    print()

    student2.get_a_mark(10, 'Ручное тестирование')
    student2.get_a_mark(9, 'Основы python')
    student2.get_a_mark(7, 'Базы данных')
    student2.display_student_marks()
