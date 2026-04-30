from multiprocessing import Process, Queue
import time


def producer(queue: Queue):
    for i in range(5):
        print(f'Производитель отправляет: {i}')
        queue.put(i)  # Помещаем данные в очередь
        time.sleep(1)
    queue.put('DONE')


def consumer(queue: Queue):
    while True:
        item = queue.get()
        if item == "DONE":
            break
        print(f'Потребитель получил: {item}')


if __name__ == '__main__':
    int_queue = Queue()

    # Запускаем два процесса: производитель и потребитель
    prod_process = Process(target=producer, args=(int_queue,))
    cons_process = Process(target=consumer, args=(int_queue,))

    prod_process.start()
    cons_process.start()

    # Ожидаем завершения процессов
    prod_process.join()
    # user_command = input('Введите DONE для остановки обработчика: ')  # >> DONE
    # int_queue.put(user_command)

    cons_process.join()
    print('Обмен данными завершен.')
