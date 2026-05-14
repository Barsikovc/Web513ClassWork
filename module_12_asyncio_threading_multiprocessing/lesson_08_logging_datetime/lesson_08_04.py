import logging


def file_logger():
    # Создание логгера
    logger = logging.getLogger('example_logger')
    logger.setLevel(level=logging.DEBUG)

    # Создание обработчика для вывода в консоль
    file_handler = logging.FileHandler(filename=r'logs\app.log', encoding='utf-8')  # НЕ ЗАБЫВАЕМ
    file_handler.setLevel(level=logging.WARNING)

    # Форматирование сообщений
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавление обработчика к логгеру
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    app_logger = file_logger()
    app_logger.debug('Это сообщение DEBUG')
    app_logger.info('Это сообщение INFO')
    app_logger.warning('Это сообщение WARNING')
    app_logger.error('Это сообщение ERROR')
    app_logger.critical('Это сообщение CRITICAL')
