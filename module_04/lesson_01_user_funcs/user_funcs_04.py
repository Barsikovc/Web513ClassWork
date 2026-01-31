import random


def get_random_gift():
    gifts = ['барбариски', "мячик", "машинка", "конструктор"]
    gift = random.sample(gifts, 1)[0]
    return gift


if __name__ == '__main__':
    while True:
        if input("Нажмите enter или введите 'stop' для остановки программы: ") == 'stop':
            break
        user_gift = get_random_gift()
        print(f'Вы получили: {user_gift}')
