def display_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'], kwargs['surname'], kwargs['age'], kwargs['phone'])


if __name__ == '__main__':
    display_personal_data(name='Иван', surname='Иванов', age=35, phone="+7(901)1234567")
