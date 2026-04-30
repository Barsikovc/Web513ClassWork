from multiprocessing import Process
import time


def long_task():
    print(f'Процесс начал работу')
    time.sleep(10)
    print(f'Процесс завершил работу.')


if __name__ == '__main__':  # !!!!обязательно для работы с процессами!!!!
    process = Process(target=long_task)
    process.start()

    # Проверяем, работает ли процесс
    if process.is_alive():
        time.sleep(2)
        user_choice = input('Процесс все еще работает. Прервать его 1 - да, 2 - нет: ')
        if user_choice == '1':
            process.terminate()
            print(f'Процесс принудительно завершен')
        else:
            print('Процесс продолжает работу')

    process.join()
    print(f'Работа завершена.')
