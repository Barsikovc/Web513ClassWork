def password_protected(password):
    def inner():
        if password == 'secret':
            print('Access granted')
        else:
            print('Access denied')

    return inner


if __name__ == '__main__':
    login = password_protected('wrong')
    login()
    print()
    login1 = password_protected('secret')
    login1()
