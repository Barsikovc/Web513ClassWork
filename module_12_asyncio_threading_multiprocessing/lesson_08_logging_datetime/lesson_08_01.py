import logging

# настройка базового конфигуратора
logging.basicConfig(level=logging.DEBUG)

logging.debug('Отладка')
logging.info('Информация')
logging.warning('Предупреждение')
logging.error('Ошибка')
logging.critical('Критическая ошибка')
