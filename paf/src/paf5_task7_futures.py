""" PAF-5
Разработать многопоточное приложение. Все сущности, желающие получить доступ к ресурсу, должны быть потоками.
Использовать возможности ООП. Приложение должно быть консольным. Использовать возможность модуля concurrent.futures.

Автостоянка. Доступно несколько машиномест. На одном месте может находиться только один автомобиль.
Если все места заняты, то автомобиль не станет ждать больше определенного времени и уедет на другую стоянку.
"""
from colorama import Fore, Style
import concurrent.futures
import random
import time


def park_a_car(name, waiting_time, parking_time):
    print(f" Car '{name}' {Fore.BLUE}arriving to parking{Style.RESET_ALL} "
          f"(can wait for {waiting_time} seconds)...")
    start = time.time()
    while (time.time() - start) < waiting_time:
        try:
            parking.pop()
        except IndexError:
            time.sleep(0.1)
        else:
            print(f" Car '{name}' {Fore.YELLOW}is parked{Style.RESET_ALL} for {parking_time} seconds...")
            time.sleep(parking_time)
            print(f" Car '{name}' {Fore.GREEN}leaving parking{Style.RESET_ALL} "
                  f"after {parking_time} seconds...")
            parking.append(1)
            return
    print(f" Car '{name}' {Fore.RED}can't wait anymore{Style.RESET_ALL} "
          f"(waited for {waiting_time} seconds)...")


number_of_cars = 10
number_of_parking_places = 4

parking = number_of_parking_places * [1]
cars = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(number_of_cars):
        arrival_interval = random.random()
        waiting_time = random.randint(3, 8)
        parking_time = random.randint(5, 10)
        time.sleep(arrival_interval)
        car = executor.submit(park_a_car, i+1, waiting_time, parking_time)
        cars.append(car)
    concurrent.futures.wait(cars)
