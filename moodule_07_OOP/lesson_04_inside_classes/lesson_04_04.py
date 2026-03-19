from lesson_04_03 import Classy

if __name__ == '__main__':
    print(Classy.__module__)
    classy_obj = Classy('ClassyObj')
    print(type(classy_obj).__module__)
