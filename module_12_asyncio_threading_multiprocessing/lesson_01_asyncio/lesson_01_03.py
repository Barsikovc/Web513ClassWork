"""
Создание Task
"""

import asyncio
from datetime import datetime


async def my_coroutine(sleep_time):
    print(f'Start {sleep_time}')
    await asyncio.sleep(sleep_time)  # Приостанавливаем выполнение на 1 секунду
    print(f"End {sleep_time}")


async def main():
    print(datetime.now())
    # Создаём таску из корутины
    task1 = asyncio.create_task(my_coroutine(3))
    task2 = asyncio.create_task(my_coroutine(1))

    await task1
    await task2
    print(datetime.now())


if __name__ == '__main__':
    # Запуск корутины
    asyncio.run(main())
