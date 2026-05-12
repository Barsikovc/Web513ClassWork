import socket

HOST = "127.0.0.1"
PORT = 50432

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_socket:
        serv_socket.bind((HOST, PORT))
        serv_socket.listen()
        while True:
            print('Ожидаю соединения...')
            sock, addr = serv_socket.accept()
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