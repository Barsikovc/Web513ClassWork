"""
Задача: реализовать менеджер контекста,
который будет пытаться (использовать библиотеку random) несколько раз установить соединение с API в случае неудачи.
Если соединение не удаётся установить после нескольких попыток, программа должна выбросить исключение.
"""
import time
from random import random


class APIConnection:
    def __init__(self, retries: int, delay: float):
        self.retries = retries
        self.delay = delay
        self.connection = None

    def __enter__(self):
        for _ in range(self.retries):
            try:
                print(f'Попытка подключения к API')
                if random() > 0.5:
                    raise ConnectionError("Не удалось подключится к API")
                self.connection = 'Соединение с API установлено'
                print(self.connection)
                return self.connection
            except ConnectionError as e:
                print(e)
                print(f'Повторная попытка через {self.delay} сек.')
                time.sleep(self.delay)
        raise ConnectionError('API недоступен')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection = None
            print(f'Соединение с API закрыто')


if __name__ == '__main__':
    with APIConnection(5, 2) as conn:
        print(f'{conn = }')
