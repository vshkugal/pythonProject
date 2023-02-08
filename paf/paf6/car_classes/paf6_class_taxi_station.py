from paf.paf6.car_classes.paf6_class_cars import EconomyCar, ComfortCar, BusinessCar


# -------------------
# Taxi Station class
# -------------------

class TaxiStation:

    # ----------------------------
    # Initialization from the file
    # ----------------------------
    def __init__(self, file_name):
        self.taxi_depot = []
        with open(file_name) as f:
            read_all = f.read()
            cars = read_all.split('\n')
            for car in cars:
                car_detail = car.split(',')
                if car_detail[0] == 'E':
                    self.taxi_depot.append(EconomyCar(car_detail[1], car_detail[2], car_detail[3], car_detail[4]))
                elif car_detail[0] == 'C':
                    self.taxi_depot.append(ComfortCar(car_detail[1], car_detail[2], car_detail[3], car_detail[4]))
                elif car_detail[0] == 'B':
                    self.taxi_depot.append(BusinessCar(car_detail[1], car_detail[2], car_detail[3], car_detail[4]))

    # ----------------------------
    # Functionality implementation
    # ----------------------------
    def list_all_cars(self):
        for car in self.taxi_depot:
            car.car_description()

    def add_a_car(self):
        while True:
            print("Choose the type of the new car: Economy (E), Comfort (C) or Business (B) --> ", end='')
            car_type = input()
            if car_type in {'E', 'C', 'B'}:
                break
            else:
                print("Such type does not exist.")
        print("Enter new car ID: ", end='')
        car_id = input()
        print("Enter new car price: ", end='')
        car_price = input()
        print("Enter new car max speed: ", end='')
        car_speed = input()
        print("Enter new car fuel_consumption: ", end='')
        car_fuel = input()
        if car_type == 'E':
            self.taxi_depot.append(EconomyCar(car_id, car_price, car_speed, car_fuel))
        elif car_type == 'C':
            self.taxi_depot.append(ComfortCar(car_id, car_price, car_speed, car_fuel))
        elif car_type == 'B':
            self.taxi_depot.append(BusinessCar(car_id, car_price, car_speed, car_fuel))

    def find_a_car(self):
        print("Enter minimum required speed: ", end='')
        min_speed = input()
        print("Enter maximum required speed: ", end='')
        max_speed = input()
        if not min_speed:
            min_speed = 0
        if not max_speed:
            max_speed = 1000
        for car in self.taxi_depot:
            if int(min_speed) <= int(car.max_speed) <= int(max_speed):
                car.car_description()

    def count_the_expenses(self):
        cost = 0
        for car in self.taxi_depot:
            cost += int(car.price)
        print(f'The total cost of cars in Taxi Station is ${cost}')

    def sort_by_fuel_consumption(self):
        sorted_taxi_depot = sorted(self.taxi_depot, key=lambda a_car: float(a_car.fuel_consumption))
        for car in sorted_taxi_depot:
            car.car_description()

    # Can't be a static method because of switch function implementation
    def exit_station(self):
        print("Thank you for using our services! Have a nice day!")
        exit()

    # ----------------------------
    # Switch implementation
    # ----------------------------
    taxi_station_functions = {
        '1': list_all_cars,
        '2': add_a_car,
        '3': find_a_car,
        '4': count_the_expenses,
        '5': sort_by_fuel_consumption,
        '6': exit_station
    }

    def execute_function(self, option):
        return self.taxi_station_functions.get(option)(self)
