import socket
import threading

HOST = "127.0.0.1"
PORT = 50400


def handle_connection(sock, addr):
    with sock:
        print('Подключение по адресу:', addr)
        while True:
            # Receive
            try:
                data = sock.recv(1024)
            except ConnectionError:
                print(f'Клиент внезапно отключился в процессе отправки данных на сервер')
                break
            print(f'Получено: {data}, от {addr}')
            data = data.upper()
            print(f'Отправлено: {data}, по адресу: {addr}')

            try:
                sock.sendall(data)
            except ConnectionError:
                print(f'Клиент внезапно отключился не могу отправить данные')
    print("Отключение по")


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_socket:
        serv_socket.bind((HOST, PORT))
        serv_socket.listen()
        while True:
            print('Ожидаю соединения...')
            sock_, addr_ = serv_socket.accept()
            thread = threading.Thread(target=handle_connection, args=(sock_, addr_))
            print(thread)
            thread.start()
