class Classy:
    """
    Класс созданный для примера
    """
    variable = 1

    def __init__(self):
        self.var = 2

    @classmethod
    def class_method(cls):
        """
        Метод класса созданный для примера
        :return:
            None
        """
        pass

    def method(self):
        """
        Метод экземпляра (объекта) созданный для примера
        :return:
        None
        """
        pass

    def __hidden(self):
        pass


if __name__ == '__main__':
    classy_obj = Classy()
    # print(classy_obj.__dict__)
    print(Classy.__dict__)

