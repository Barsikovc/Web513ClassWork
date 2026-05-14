"""
Задача: создать систему для логирования действий пользователя в приложении.

Программа должна:

Логировать действия пользователя, такие как вход в систему, выход и изменение настроек.
Логировать дату и время каждого события.
Логировать продолжительность времени, в течение которого пользователь находился в системе (между входом и выходом).
Логировать ошибки, если действие пользователя невозможно выполнить
(например, при попытке изменения настроек приложение не отвечает).
"""

import logging
from datetime import datetime
import time


class UserSessions:

    def __init__(self, username):
        self.username = username
        self.login_time = None
        self.logout_time = None
        self.session_logger = session_logger()

    def login(self):
        self.login_time = datetime.now()
        self.session_logger.info(f'Пользователь: {self.username} вошел в систему.')

    def logout(self):
        if not self.login_time:
            self.session_logger.error(f'Ошибка: пользователь {self.username} не был авторизован.')
            return
        self.logout_time = datetime.now()
        session_duration = self.logout_time - self.login_time
        self.session_logger.info(
            f'Пользователь {self.username} вышел из системы. Продолжительность сессии: {session_duration}'
        )

    def change_settings(self, new_username):
        if not self.login_time:
            self.session_logger.error(f'Ошибка: пользователь {self.username} не авторизован для изменения настроек.')
            return
        old_name = self.username
        self.username = new_username
        self.session_logger.info(f'Пользователь: {old_name} изменил настройки имени новое имя >> {self.username}')


def session_logger():
    """
    По факту один логгер может делать все:)
    """
    # Создание логгера
    logger = logging.getLogger('user_actions')
    logger.setLevel(logging.INFO)

    # Создание обработчика для записи в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Создание обработчика для записи в файл
    file_handler = logging.FileHandler(r'logs\user_actions_log.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # Настройка формата логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


if __name__ == '__main__':
    user1 = UserSessions('Alex')
    user1.login()
    user1.change_settings('SuperAlex')
    time.sleep(5)
    user1.logout()
    print()

    user2 = UserSessions("Eva")
    user2.change_settings("NewEva")
    user2.logout()
