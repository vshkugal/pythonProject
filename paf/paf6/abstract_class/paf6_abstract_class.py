from abc import ABC, abstractmethod


# -------------------
# Abstract class car
# -------------------

class Car(ABC):
    def __init__(self, car_id, price, max_speed, fuel_consumption):
        self.car_id = car_id
        self.price = price
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def car_description(self):
        pass
