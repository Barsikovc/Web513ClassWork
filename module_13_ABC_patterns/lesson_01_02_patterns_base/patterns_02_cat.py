class Sausage:
    def __init__(self):
        self._energy = 1

    def give_energy(self):
        return self._energy


class Cat:
    def __init__(self, name, energy=0):
        self.name = name
        self.energy = energy

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            return 'Cat plays'
        return f'Need sausage'

    def eat(self, obj):
        if isinstance(obj, Sausage):
            self.energy += obj.give_energy()
            return f'Cat received {obj.give_energy()} energy. Current energy: {self.energy}'
        return 'Cat eat only Sausages'


if __name__ == '__main__':
    sausage = Sausage()
    cat = Cat('Tom')
    print(cat.play())
    print(cat.eat("food"))
    print(cat.eat(sausage))
    print(cat.play())
