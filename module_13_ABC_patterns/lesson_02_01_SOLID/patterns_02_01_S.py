"""
S - Single Responsibility Principle
Принцип единственной ответственности
"""


# class Employee:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     def print_time_sheet_report(self, report):
#         print(f'Сотрудник {self._name} печатает отчет: {report}')
#         return report
#
#
# if __name__ == '__main__':
#     employee = Employee("Дмитрий")
#     employee.print_time_sheet_report('Баланс')

class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'Сотрудник {self.name}'


class TimeSheetReport:
    @staticmethod
    def print_time_sheet_report(employee_obj, report):
        print(f'{employee_obj} печатает отчет: {report}')
        return report


if __name__ == '__main__':
    employee = Employee("Дмитрий")
    TimeSheetReport.print_time_sheet_report(employee, 'баланс')
