import logging


def stream_logger():
    # Создание логгера
    logger = logging.getLogger('example_logger')
    logger.setLevel(level=logging.DEBUG)

    # Создание обработчика для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level=logging.INFO)

    # Форматирование сообщений
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Добавление обработчика к логгеру
    logger.addHandler(console_handler)
    return logger


if __name__ == '__main__':
    app_logger = stream_logger()
    app_logger.debug('Это сообщение DEBUG')
    app_logger.info('Это сообщение INFO')
    app_logger.warning('Это сообщение WARNING')
