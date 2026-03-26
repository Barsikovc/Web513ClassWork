class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedLandVehicle(LandVehicle):
    pass


def is_instance(obj_list, cls_list):
    for obj in obj_list:
        for cls in cls_list:
            print(isinstance(obj, cls), end='\t')
        print()


if __name__ == '__main__':
    v_obj = Vehicle()
    lv_obj = LandVehicle()
    tlv_obj = TrackedLandVehicle()
    my_obj_list = [v_obj, lv_obj, tlv_obj]
    my_cls_list = [Vehicle, LandVehicle, TrackedLandVehicle]
    is_instance(obj_list=my_obj_list, cls_list=my_cls_list)
