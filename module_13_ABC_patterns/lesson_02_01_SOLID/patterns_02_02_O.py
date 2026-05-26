"""
O - Open/Closed Principle
"""


class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'Сотрудник {self.name}'


class SurnameEmployee(Employee):
    def __init__(self, name, surname):
        super().__init__(name)
        self._surname = surname

    @property
    def surname(self):
        return self._surname

    def __str__(self):
        base = super().__str__()
        return f'{base} {self.surname}'


class TimeSheetReport:
    @staticmethod
    def print_time_sheet_report(employee_obj, report):
        if isinstance(employee_obj, Employee):
            print(f'{employee_obj} печатает отчет: {report}')
            return report
        print('Такая сущность мне незнакома')
        return None


if __name__ == '__main__':
    employee = Employee("Дмитрий")
    TimeSheetReport.print_time_sheet_report(employee, 'баланс')
    print()

    employee_s = SurnameEmployee('Дмитрий', 'Сульжиц')
    TimeSheetReport.print_time_sheet_report(employee_s, 'баланс')
    print()

    TimeSheetReport.print_time_sheet_report('Сотрудник', 'баланс')
