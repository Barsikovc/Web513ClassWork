def combine_employee_data(names, positions, salaries):
    combined = zip(names, positions, salaries)
    return list(map(lambda x: f'Имя: {x[0]} - должность: {x[1]} - зарплата: {x[2]}', combined))


if __name__ == '__main__':
    emp_names = ["Анна", "Борис", "Виктория"]
    emp_positions = ["Менеджер", "Разработчик", "Аналитик"]
    emp_salaries = [80000, 120000, 90000]

    for employee in combine_employee_data(emp_names, emp_positions, emp_salaries):
        print(employee)
