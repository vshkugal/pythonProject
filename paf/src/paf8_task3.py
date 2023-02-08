"""PAF-8: Генератор
Написать аналог range (не используя range/xrange внутри).
Функция принимает 1, 2 или 3 позиционных аргумента соответственно, и возвращает генератор.
Если аргумент 1 – это число стоп, если 2 – старт и стоп, если 3 то старт, стоп и шаг.
Проверить возможные комбинации аргументов, генератор не должен виснуть (в бесконечном цикле) при невалидных комбинациях.
Развернуть генератор можно в цикле for или сконвертировать его в list/tuple.
"""
from typing import Generator, Union


def my_range(stop_number: Union[int, float], start_number: Union[int, float] = None, step: Union[int, float] = 1) \
        -> Generator[Union[int, float], None, None]:
    """
    Range generator function

    :param stop_number:  int / float
    :param start_number:  int / float, default value 0
    :param step:  int / float, default value 1
    :return: generator int / float
    """
    if step == 0:
        raise ValueError("You can't increment by 0")

    current_number, stop = (0, stop_number) if start_number is None else (stop_number, start_number)

    if not isinstance(current_number, (int, float)) or not isinstance(stop, (int, float)) \
            or not isinstance(step, (int, float)):
        raise ValueError("Only numbers are allowed as arguments")

    if step > 0:
        def check(arg_left, arg_right): return arg_left < arg_right
    else:
        def check(arg_left, arg_right): return arg_left > arg_right

    while check(current_number, stop):
        yield current_number
        current_number += step

print([i for i in my_range(10)])
print([i for i in my_range(5, 10)])
print([i for i in my_range(3, 10, 2)])
print([i for i in my_range(15, 5)])
print([i for i in my_range(15, 5, -1)])
print([i for i in my_range(10, 0, -1)])
print([i for i in my_range(10, 0, 1)])
print([i for i in my_range(0, 10, 1)])
print([i for i in my_range(-10, 0, -1)])
print([i for i in my_range(-10)])
print([i for i in my_range(-10, 0, 1)])
print([i for i in my_range(5, -5, -1)])
# print([i for i in my_range(5, 10, 0)])
print([i for i in my_range(5.5, 10.5, 0.5)])
print([i for i in my_range(1, 10, 2.5)])

print([i for i in my_range(30, 2)])
print([i for i in my_range(8, 2, -3)])
print([i for i in my_range(9, 999, 7)])
# print([i for i in my_range('a')])
