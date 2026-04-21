from _03_pickle_classes import Pickler, UnPickler
from module_11_data_packing.lesson_01_pickle._02_pickle_difficult._02_pickle_difficult import DoubleLinkedList

if __name__ == '__main__':
    pickler_5 = Pickler(protocol=5)
    pickler_default = Pickler()

    my_ll = DoubleLinkedList()
    my_ll.insert_at_head("Барсик_01")
    my_ll.insert_at_head("Снежок_00")
    my_ll.insert_at_tail('Франц_03')

    my_ll = pickler_5.pickle_data(my_ll)
    print(my_ll)
    my_ll = UnPickler.unpickle_data(my_ll)
    my_ll.print_ll_from_head()
    print()

    pickler_default.pickle_data_to_file('ll_pickle.cats', my_ll)
    my_ll_ff = UnPickler.unpickle_file('ll_pickle.cats')
    my_ll.print_ll_from_tail()
