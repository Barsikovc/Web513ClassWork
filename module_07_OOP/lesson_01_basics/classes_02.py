class CakeForm:

    def __init__(self, dough, form):
        self.dough = dough
        self.form = form
        print(f'Я кекс из теста: {self.dough}, в форме: {self.form}')

    def make_dough(self):
        return f'Мы замешиваем тесто'

    def make_form(self):
        return f'Мы выкладываем тесто в форму'

    def cook_cake(self, time=40):
        if time > 80:
            return f'За {time} минут кекс сгорит!'
        return f'Мы выпекаем кекс {time} минут'


if __name__ == '__main__':
    cake_1 = CakeForm("Пшеничное", "Круглая")
    cake_2 = CakeForm("Овсяное", "Квадратная")






