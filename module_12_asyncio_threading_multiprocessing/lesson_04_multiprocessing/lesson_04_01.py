from multiprocessing import Process


def say_hello():
    print(f'Привет от процесса')


if __name__ == '__main__':  # !!!!обязательно для работы с процессами!!!!
    process = Process(target=say_hello)
    process.start()
    process.join()
