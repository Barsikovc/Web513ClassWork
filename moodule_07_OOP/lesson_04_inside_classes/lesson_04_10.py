class One:
    def __init__(self, name):
        self.name = name

    def do_it(self):
        print(f'do it from {self.name}: (ONE)')

    def do_anything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print(f'do it from {self.name}: (TWO)')


if __name__ == '__main__':
    one = One('obj_one')
    two = Two('obj_two')
    one.do_anything()
    two.do_anything()
