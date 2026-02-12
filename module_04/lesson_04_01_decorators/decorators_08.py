"""
Ситуация: мы разрабатываем приложение, которое отслеживает действия пользователей,
такие как вход в систему, обновление профиля или отправка сообщения.
Для каждого действия нужно сохранять лог с именем пользователя и названием выполненной функции.
Лог-файлы позволяют анализировать действия пользователей и выявлять ошибки в работе системы.

Задача: создать декоратор log_action, который:

Логирует имя пользователя и выполняемое действие.
Сохраняет эту информацию в текстовый файл actions.log.
Работает с любыми функциями, которые принимают username как первый аргумент.
"""
from datetime import datetime
from functools import wraps


def log_action(func):
    @wraps(func)
    def wrapper(username, *args, **kwargs):
        if not args and not kwargs:
            log_string = f'{datetime.now()} >> User: {username}. action: {func.__name__}\n'
        else:
            log_string = f'{datetime.now()} >> User: {username}. action: {func.__name__}, params ({args}/{kwargs})\n'
        with open(r'logs\actions.log', 'a', encoding='utf-8') as log_file:
            log_file.write(log_string)
        return func(username, *args, **kwargs)

    return wrapper


@log_action
def login(username):
    print(f'{username} вошел в систему')


@log_action
def update_profile(username, name, age):
    print(f'{username} обновил профиль с данными: {name} {age}')


if __name__ == '__main__':
    login('Alice')
    update_profile("Alice", "Алиса", age=25)
