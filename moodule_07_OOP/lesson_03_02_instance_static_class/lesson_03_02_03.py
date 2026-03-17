class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        BankAccount.is_valid_amount(amount)
        self.balance += amount
        print(f'{self.owner} пополнил счет на {amount} >> Новый баланс: {self.balance}')

    @classmethod
    def set_interest_rate(cls, new_rate):
        if new_rate > 0:
            cls.interest_rate = new_rate
        else:
            raise ValueError('Процентная ставка должна быть положительной!')

    @staticmethod
    def is_valid_amount(amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('Неверный тип данных')
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть больше 0')
        return True


if __name__ == '__main__':
    account = BankAccount('Иван', 1000)
    account.deposit(500)
    BankAccount.set_interest_rate(0.07)
    # print(BankAccount.is_valid_amount(600.50))
    # print(BankAccount.is_valid_amount(600))
    account.deposit(600.50)
    # BankAccount.set_interest_rate(-0.1)

