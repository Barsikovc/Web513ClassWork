class CakeForm:
    def __init__(self, dough, form, *args):
        self.dough = dough
        self.form = form
        if not args:
            self.ingredient_list = []
        else:
            self.ingredient_list = list(args)

    def make_dough(self):
        return f'Мы замешаем тесто: {self.dough}'

    def make_form(self):
        return f'Мы выкладываем тесто в форму {self.form}'

    def add_ingredient(self, ingredient):
        self.ingredient_list.append(ingredient)
        return f'Добавлен {ingredient}'

    def add_ingredients(self, *args):
        self.ingredient_list.extend(args)
        return f'Добавлены: {', '.join(args)}'

    def cook_cake(self, time=40):
        if not self.ingredient_list:
            if time > 80:
                return f'За {time} минут кекс из теста: {self.dough}, формы {self.form} сгорит :('
            return f'Мы выпекаем кекс из теста: {self.dough}, формы {self.form} {time} минут'
        else:
            if time > 80:
                return f'За {time} минут кекс из теста: {self.dough}, формы {self.form}, дополнительно: {', '.join(self.ingredient_list)}  сгорит :('
            return f'Мы выпекаем кекс из теста: {self.dough}, формы {self.form}, дополнительно: {', '.join(self.ingredient_list)} {time} минут'


# if __name__ == '__main__':
#     cake_1 = CakeForm("Пшеничное", "Круглая")
#     cake_2 = CakeForm("Овсяное", "Квадратная")
