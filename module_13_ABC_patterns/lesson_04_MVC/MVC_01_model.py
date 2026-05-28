import json


class MarksModel:
    all_students = []

    def __init__(self, student_email):
        self.__student_email = student_email
        self.__student_marks = []
        MarksModel.all_students.append({student_email: self.__student_marks})

    @property
    def student_email(self):
        return self.__student_email

    @property
    def student_marks(self):
        return self.__student_marks

    def add_mark(self, course, mark):
        data = {}
        data['course'] = course
        data['mark'] = mark
        self.student_marks.append(data)
        # self.update_json()

    # костыль для имитации разных запусков
    def clear_marks(self):
        self.student_marks.clear()

    def update_json(self):
        try:
            with open(rf'student_marks\{self.student_email}_marks.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            print(data)
            self.student_marks.extend(data)
        except Exception as ex:
            print(ex)
        with open(rf'student_marks\{self.student_email}_marks.json', 'w', encoding='utf-8') as file:
            json.dump(self.student_marks, file, ensure_ascii=False, indent=4)

    @classmethod
    def save_all_students_data(cls):
        with open(rf'student_marks\all_students_data.json', 'w', encoding='utf-8') as file:
            json.dump(cls.all_students, file, ensure_ascii=False, indent=4)

    def calculate_average_mark(self):
        overall_score = 0
        for mark in self.student_marks:
            overall_score += mark['mark']
        return round(overall_score / len(self.student_marks), 2)


# if __name__ == '__main__':
    # user_email = input('Введите вашу почту: ')
    # user_email = 'mail@yandex.ru'
    # marks_model = MarksModel(user_email)
    # marks_model.add_mark('HTML', 10)
    # marks_model.add_mark('CSS', 12)
    # marks_model.add_mark('JavaScript', 9)
    # marks_model.add_mark('Python', 11)
    # marks_model.update_json()
    # print(marks_model.student_marks)
    # print(marks_model.calculate_average_mark())
    # marks_model.clear_marks()  # имитация перезапуска
    # marks_model.add_mark('JavaScript', 9)
    # marks_model.add_mark('Python', 11)
    # marks_model.update_json()
