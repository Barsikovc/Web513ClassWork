"""
Ситуация: мы работаем с подключениями к базе данных и должны гарантировать,
что соединение будет закрыто после работы независимо от того, возникли ли ошибки.

Задача — реализовать менеджер контекста для управления соединением с базой данных (имитация).
"""


class DBConnection:
    def __init__(self, user, password, driver, server, db_name):
        self.user = user
        self.password = password
        self.driver = driver
        self.server = server
        self.db_name = db_name

    def __enter__(self):
        print(f'Открываем соединение с базой данных: {self.db_name}')
        print(f'Данные для аутентификации:')
        print(f"""DRIVER={self.driver};
SERVER={self.server};
DATABASE={self.db_name};
UID={self.user};
PWD={self.password}""")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Закрываем соединение с базой данных: {self.db_name}')
        if exc_type:
            print(f'Произошла ошибка: {exc_type.__name__}: {exc_val}')
            return False
        return True


if __name__ == '__main__':
    params = {
        'user': 'dsulzhyts',
        'password': 'qwerty',
        'driver': 'pyodbc',
        'server': r'DESKTOP-C7FGGRN\SQLEXPRESS',
        'db_name': 'my_db',
    }

    with DBConnection(**params):
        print(f'Работаем с БД')
        # raise Exception('что-то пошло не так!')
