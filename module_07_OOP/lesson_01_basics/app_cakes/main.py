from Classes.ClassCake import CakeForm


if __name__ == '__main__':
    cake_1 = CakeForm("Пшеничное", "Круглая", 'Ром', 'Марципан')
    print(cake_1.make_dough())
    print(cake_1.make_form())
    print(cake_1.add_ingredient('Изюм'))
    print(cake_1.add_ingredients('Курага', 'Чернослив'))
    print()
    print(cake_1.cook_cake())
    print(cake_1.cook_cake(100))
    print()

    cake_2 = CakeForm("Овсяное", "Квадратная")
    print(cake_2.make_dough())
    print(cake_2.make_form())
    print(cake_2.cook_cake())
    print(cake_2.cook_cake())