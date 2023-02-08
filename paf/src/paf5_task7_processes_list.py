""" PAF-5
Разработать многопроцессное приложение. Все сущности, желающие получить доступ к ресурсу, должны быть процессами.
Использовать возможности ООП. Приложение должно быть консольным. Использовать возможность модуля multiprocessing.

Автостоянка. Доступно несколько машиномест. На одном месте может находиться только один автомобиль.
Если все места заняты, то автомобиль не станет ждать больше определенного времени и уедет на другую стоянку.
"""
from colorama import Fore, Style
import multiprocessing
import random
import time


class Car(multiprocessing.Process):
    def __init__(self, name, car_waiting_time, car_parking_time, car_parking):
        super().__init__()
        self.name = name
        self.waiting_time = car_waiting_time
        self.parking_time = car_parking_time
        self.parking = car_parking

    def run(self):
        print(f" Car '{self.name}' {Fore.BLUE}arriving to parking{Style.RESET_ALL} "
              f"(can wait for {self.waiting_time} seconds)...")
        start = time.time()
        while (time.time() - start) < self.waiting_time:
            try:
                self.parking.pop()
            except IndexError:
                time.sleep(0.1)
            else:
                print(f" Car '{self.name}' {Fore.YELLOW}is parked{Style.RESET_ALL} for {self.parking_time} seconds...")
                time.sleep(self.parking_time)
                print(f" Car '{self.name}' {Fore.GREEN}leaving parking{Style.RESET_ALL} "
                      f"after {self.parking_time} seconds...")
                self.parking.append(1)
                return
        print(f" Car '{self.name}' {Fore.RED}can't wait anymore{Style.RESET_ALL} "
              f"(waited for {self.waiting_time} seconds)...")


if __name__ == '__main__':

    number_of_cars = 10
    number_of_parking_places = 4

    parking = multiprocessing.Manager().list(number_of_parking_places * [1])
    processes = []

    for i in range(number_of_cars):
        arrival_interval = random.random()
        waiting_time = random.randint(3, 8)
        parking_time = random.randint(5, 10)
        time.sleep(arrival_interval)
        car = Car(str(i+1), waiting_time, parking_time, parking)
        car.start()
        processes.append(car)

    for process in processes:
        process.join()
