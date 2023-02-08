from paf.paf6.abstract_class.paf6_abstract_class import Car


# -------------------
# Economy class car
# -------------------

class EconomyCar(Car):
    def __init__(self, car_id, price, max_speed, fuel_consumption):
        super().__init__(car_id, price, max_speed, fuel_consumption)
        self.type = 'Economy'

    def car_description(self):
        print(f"Car ID: {self.car_id}\t\tType: {self.type}\tPrice: ${self.price}\t"
              f"Max speed: {self.max_speed}km/h\tFuel consumption: {self.fuel_consumption}l")


# -------------------
# Comfort class car
# -------------------

class ComfortCar(EconomyCar):
    def __init__(self, car_id, price, max_speed, fuel_consumption):
        super().__init__(car_id, price, max_speed, fuel_consumption)
        self.type = 'Comfort'
        self.music = 'No music'

    def choose_music(self):
        print("What music would you like to listen to?")
        self.music = input()


# -------------------
# Business class car
# -------------------

class BusinessCar(ComfortCar):
    def __init__(self, car_id, price, max_speed, fuel_consumption):
        super().__init__(car_id, price, max_speed, fuel_consumption)
        self.type = 'Business'
        self.drink = 'No drink'

    def choose_drink(self):
        print("What would you like to drink?")
        self.drink = input()
