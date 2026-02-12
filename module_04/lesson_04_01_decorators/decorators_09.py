"""
Ситуация: мы разрабатываем систему для управления секретными данными,
доступ к которым должен быть только у пользователей с правами администратора.
Необходимо автоматически проверять права доступа перед выполнением функции.

Задача: создать декоратор authorize_admin, который:

Проверяет, является ли пользователь администратором.
Если пользователь администратор, выполняет функцию.
Если пользователь не администратор, выводит сообщение «Доступ запрещён».
"""

from functools import wraps


class AccessError(Exception):
    pass


def authorise_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user[1] == 'admin':
            return func(user, *args, **kwargs)
        else:
            print(f'Access denied for: {user[0]}!')
            raise AccessError(f'Access denied for: {user[0]}!')

    return wrapper


@authorise_admin
def view_secret_data(user):
    print(f'Secret data for {user[0]}, status {user[1]}')


if __name__ == '__main__':
    view_secret_data(['Alice', 'admin'])
    view_secret_data(['Bob', 'manager'])
