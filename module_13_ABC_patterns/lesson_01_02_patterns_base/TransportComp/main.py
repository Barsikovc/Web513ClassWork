from classes_01_transport import *
from classes_02_driver import *
from classes_03_engine import *

if __name__ == '__main__':
    engine = CombustionEngine()
    driver = HumanDriver()
    car = Car(engine, driver)
