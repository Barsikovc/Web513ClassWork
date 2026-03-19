"""
Композиция
"""

import time


class Tracks:
    def change_direction(self, track, on):
        print(f'tracks: {track} {on}')


class Wheels:
    def change_direction(self, direction, on):
        print(f'wheels: {direction} {on}')


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, param, on):
        self.controller.change_direction(param, on)
        time.sleep(on)
        self.controller.change_direction(param, on)


if __name__ == '__main__':
    tracked = Vehicle(Tracks())
    wheeled = Vehicle(Wheels())
    tracked.turn('left', 3)
    wheeled.turn('right', 2)
