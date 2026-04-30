from multiprocessing import Process, Pipe
import time


def sender(conn: Pipe):
    for i in range(5):
        print(f'Отправитель отправляет: {i}')
        conn.send(i)  # Отправляем данные через канал
        time.sleep(1)
    # conn.send("DONE")

def receiver(conn: Pipe):
    while True:
        data = conn.recv()  # Получаем данные из канала
        if data == "DONE":
            break
        print(f'Получатель получил: {data}')


if __name__ == '__main__':
    # Создаём канал связи
    parent_conn, child_conn = Pipe()

    # Запускаем два процесса: производитель и потребитель
    send_process = Process(target=sender, args=(parent_conn,))
    recv_process = Process(target=receiver, args=(child_conn,))

    send_process.start()
    recv_process.start()

    # Ожидаем завершения процессов
    send_process.join()
    user_command = input('Введите DONE для остановки обработчика: ')  # >> DONE
    parent_conn.send(user_command)

    recv_process.join()
    print('Обмен данными завершен.')
