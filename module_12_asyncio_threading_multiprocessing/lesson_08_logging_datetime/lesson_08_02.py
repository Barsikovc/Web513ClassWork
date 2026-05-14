import logging

# настройка базового конфигуратора
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# %(asctime)s — время записи сообщения.
# %(levelname)s — уровень важности сообщения (например, DEBUG, INFO).
# %(message)s — текст сообщения.
# %(filename)s — имя файла, из которого было вызвано лог-сообщение.
# %(lineno)d — номер строки, где было вызвано лог-сообщение.

logging.debug('Отладка')
logging.info('Информация')
logging.warning('Предупреждение')
logging.error('Ошибка')
logging.critical('Критическая ошибка')
