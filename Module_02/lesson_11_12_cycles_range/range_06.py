from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def some_method(self):
        pass


class ConcreteClass(AbstractClass):

    def some_method(self):
        print(f'Вот и конкретный метод класса ConcreteClass')


if __name__ == '__main__':
    my_class = ConcreteClass()
    my_class.some_method()
