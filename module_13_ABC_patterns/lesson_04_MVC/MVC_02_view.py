from MVC_03_controller import MarksController


class MarksView:

    def __init__(self, controller: MarksController):
        self.controller = controller

    def display_default_action(self):
        print(f'{self.controller.get_default_action()}')

    def display_marks_auth(self, user_role='guest'):  # передача доступа обычно происходит скрытно
        result = self.controller.get_marks_auth(user_role)
        if result == 'Forbidden':
            print(result)
        elif result:
            for item in result:
                print(f'{item['course']} оценка: {item['mark']}')
        else:
            print(f'Нет данных')

    def display_only_courses_list(self):
        result = self.controller.get_only_courses_list()
        if result:
            print(f'Список курсов')
            for item in result:
                print(item, end=' ')
            print()
        else:
            print(f'Курсов нет!')

    def display_only_marks_list(self):
        result = self.controller.get_only_marks_list()
        if result == 'Forbidden':
            print(result)
        elif result:
            print(f'Список оценок:')
            for item in result:
                print(item, end=' ')
            print()
        else:
            print(f'Оценок нет!')

    def display_all_data_list(self, user_role='guest'):
        result = self.controller.get_all_data_list(user_role)
        if result:
            print(result)
        else:
            print(f'Нет данных!')

    def display_add_mark(self, course, mark, user_role='guest'):
        if not isinstance(mark, int):
            print(f'Неверный тип данных')
        elif not 1 <= mark <= 12:
            print(f'Оценка должна быть в диапазоне от 1 до 12 (включительно)')
        else:
            result = self.controller.add_mark(course, mark, user_role)
            if result is False:
                print(f'Ошибка ввода')
            elif result == 'Forbidden':
                print(result)
            else:
                print(f'Оценка успешно добавлена: {course}, {mark}')

