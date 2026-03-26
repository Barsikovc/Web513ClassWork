from abc import ABC, abstractmethod

import time


class Vehicle(ABC):

    @abstractmethod
    def change_direction(self, on):
        pass

    def turn(self, on):
        self.change_direction(on)
        time.sleep(1)
        self.change_direction(on)


class TrackedVehicle(Vehicle):
    def control_track(self, stop):
        print(f'Я остановил гусеницу на {stop} секунд')

    def change_direction(self, on):
        self.control_track(on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(self, on):
        print(f'Я повернул колеса в направлении {on}')

    def change_direction(self, on):
        self.turn_front_wheels(on)


if __name__ == '__main__':
    tracked = TrackedVehicle()
    wheeled = WheeledVehicle()

    tracked.turn('3')
    wheeled.turn('left')
