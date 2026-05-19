class Sausage:
    def __init__(self):
        self._energy = 1

    def give_energy(self):
        return self._energy


class Chicken:
    def __init__(self):
        self._energy = 2

    def give_energy(self):
        return self._energy


class Food:
    def __init__(self, food):
        self.food = food

    def give_energy(self):
        return self.food.give_energy()


class CatUpdate:
    def __init__(self, name, energy=0):
        self.name = name
        self.energy = energy

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            return 'Cat plays'
        return f'Need Food'

    def eat(self, obj):
        if isinstance(obj, Food):
            self.energy += obj.give_energy()
            return f'Cat received {obj.give_energy()} energy. Current energy: {self.energy}'
        return 'Cat eat only Food'


if __name__ == '__main__':
    sausage = Sausage()
    chicken = Chicken()
    food_sausage = Food(sausage)
    food_chicken = Food(chicken)

    cat = CatUpdate('Tom')
    print(cat.play())
    print(cat.eat("food"))
    print(cat.eat(food_sausage))
    print(cat.play())
    print(cat.play())
    print()
    print(cat.eat(food_chicken))
    print(cat.play())

