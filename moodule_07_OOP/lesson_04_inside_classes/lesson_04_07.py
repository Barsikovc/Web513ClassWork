class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedLandVehicle(LandVehicle):
    pass


def is_subclass(cls_list):
    for cls1 in cls_list:
        for cls2 in cls_list:
            print(issubclass(cls1, cls2), end='\t')
        print()


if __name__ == '__main__':
    my_cls_list = [Vehicle, LandVehicle, TrackedLandVehicle]
    is_subclass(cls_list=my_cls_list)
