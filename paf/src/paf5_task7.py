""" PAF-5
Разработать многопоточное приложение. Все сущности, желающие получить доступ к ресурсу, должны быть потоками.
Использовать возможности ООП. Приложение должно быть консольным. Использовать возможность модуля threading.

Автостоянка. Доступно несколько машиномест. На одном месте может находиться только один автомобиль.
Если все места заняты, то автомобиль не станет ждать больше определенного времени и уедет на другую стоянку.
"""
from colorama import Fore, Style
import random
import threading
import time


class Car(threading.Thread):
    def __init__(self, name, car_waiting_time, car_parking_time):
        threading.Thread.__init__(self)
        self.name = name
        self.waiting_time = car_waiting_time
        self.parking_time = car_parking_time

    def run(self):
        # Console output without colors
        # print(f" Car '{self.name}' arriving to parking (can wait for {self.waiting_time} seconds)...")
        # if not parking.acquire(timeout=self.waiting_time):
        #     print(f" Car '{self.name}' can't wait anymore (waited for {self.waiting_time} seconds)...")
        #     return
        # print(f" Car '{self.name}' is parked for {self.parking_time} seconds...")
        # time.sleep(self.parking_time)
        # print(f" Car '{self.name}' leaving parking after {self.parking_time} seconds...")
        # parking.release()

        # Console output using different colors for different actions
        print(f" Car '{self.name}' {Fore.BLUE}arriving to parking{Style.RESET_ALL} "
              f"(can wait for {self.waiting_time} seconds)...")
        if not parking.acquire(timeout=self.waiting_time):
            print(f" Car '{self.name}' {Fore.RED}can't wait anymore{Style.RESET_ALL} "
                  f"(waited for {self.waiting_time} seconds)...")
            return
        print(f" Car '{self.name}' {Fore.YELLOW}is parked{Style.RESET_ALL} for {self.parking_time} seconds...")
        time.sleep(self.parking_time)
        print(f" Car '{self.name}' {Fore.GREEN}leaving parking{Style.RESET_ALL} after {self.parking_time} seconds...")
        parking.release()


number_of_cars = 10
number_of_parking_places = 4

# parking = threading.Semaphore(value=number_of_parking_places)
parking = threading.BoundedSemaphore(value=number_of_parking_places)

threads = []

for i in range(number_of_cars):
    arrival_interval = random.random()
    waiting_time = random.randint(3, 8)
    parking_time = random.randint(5, 10)
    time.sleep(arrival_interval)
    car = Car(str(i+1), waiting_time, parking_time)
    car.start()
    threads.append(car)

for thread in threads:
    thread.join()
