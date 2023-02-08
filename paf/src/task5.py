"""
Написать функцию, принимающую строку и возвращающую количество вхождений в неё символов.
"""


def count_symbols_quantity_dict(string: str):
    symbols_quantity = {}
    for symbol in string:
        if symbol in symbols_quantity.keys():
            symbols_quantity[symbol] += 1
        else:
            symbols_quantity.update({symbol: 1})
    return symbols_quantity


def count_symbols_quantity_dict_shorter1(string: str):
    symbols_quantity = {}
    for symbol in string:
        if symbol not in symbols_quantity.keys():
            symbols_quantity.update({symbol: 0})
        symbols_quantity[symbol] += 1
    return symbols_quantity


def count_symbols_quantity_dict_shorter2(string: str):
    symbols_quantity = {}
    for symbol in string:
        if symbol not in symbols_quantity.keys():
            symbols_quantity[symbol] = 0
        symbols_quantity[symbol] += 1
    return symbols_quantity


def count_symbols_quantity_list(string: str):
    symbols, quantity = [], []
    for symbol in string:
        if symbol in symbols:
            i = symbols.index(symbol)
            quantity[i] += 1
        else:
            symbols.append(symbol)
            quantity.append(1)
    return symbols, quantity


def print_symbols_quantity_list(symbols, quantity):
    print()
    for i in range(len(symbols)):
        print("Symbol: '" + str(symbols[i]) + "', quantity: " + str(quantity[i]))
