import pytest
from ..src.task5 import *

test_data_dict = {
    "1":
        {"String": "hsdfzjlheuihuvkjzhdh",
         "Result": {'h': 5, 's': 1, 'd': 2, 'f': 1, 'z': 2, 'j': 2, 'l': 1, 'e': 1, 'u': 2, 'i': 1, 'v': 1, 'k': 1}},
    "2":
        {"String": "asdfgasdfgasd", "Result": {'a': 3, 's': 3, 'd': 3, 'f': 2, 'g': 2}},
    "3":
        {"String": "aaaaaaaaaassssssss", "Result": {'a': 10, 's': 8}},
    "4":
        {"String": "1234567890-=1234567890-=",
         "Result": {'1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, '0': 2, '-': 2, '=': 2}},
    "5":
        {"String": "'''''''''''rrr'''''''''''''", "Result": {"'": 24, 'r': 3}},
    "6":
        {"String": "   ", "Result": {' ': 3}},
    "7":
        {"String": "\n", "Result": {'\n': 1}},
    "8":
        {"String": "", "Result": {}}
}

test_data_list = {
    "1":
        {"String": "hsdfzjlheuihuvkjzhdh",
         "Symbols": ['h', 's', 'd', 'f', 'z', 'j', 'l', 'e', 'u', 'i', 'v', 'k'],
         "Quantity": [5, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1]},
    "2":
        {"String": "asdfgasdfgasd", "Symbols": ['a', 's', 'd', 'f', 'g'], "Quantity": [3, 3, 3, 2, 2]},
    "3":
        {"String": "aaaaaaaaaassssssss", "Symbols": ['a', 's'], "Quantity": [10, 8]},
    "4":
        {"String": "1234567890-=1234567890-=",
         "Symbols": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
         "Quantity": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]},
    "5":
        {"String": "'''''''''''rrr'''''''''''''", "Symbols": ["'", 'r'], "Quantity": [24, 3]},
    "6":
        {"String": "   ", "Symbols": [' '], "Quantity": [3]},
    "7":
        {"String": "\n", "Symbols": ["\n"], "Quantity": [1]},
    "8":
        {"String": "", "Symbols": [], "Quantity": []}
}


@pytest.mark.parametrize("string, symbols_quantity",
                         [i.values() for i in test_data_dict.values()],
                         ids=[f"Test {i[0]} | String: '{i[1]['String']}' -> Result: {i[1]['Result']}"
                              for i in zip(test_data_dict.keys(), test_data_dict.values())]
                         )
def test_symbols_quantity_dict(string, symbols_quantity):
    res = count_symbols_quantity_dict(string)
    assert res == symbols_quantity, f"Test result {res} differs from expected result {symbols_quantity}"


@pytest.mark.parametrize("string, symbols_quantity",
                         [i.values() for i in test_data_dict.values()],
                         ids=[f"Test {i[0]} | String: '{i[1]['String']}' -> Result: {i[1]['Result']}"
                              for i in zip(test_data_dict.keys(), test_data_dict.values())]
                         )
def test_symbols_quantity_dict1(string, symbols_quantity):
    res = count_symbols_quantity_dict_shorter1(string)
    assert res == symbols_quantity, f"Test result {res} differs from expected result {symbols_quantity}"


@pytest.mark.parametrize("string, symbols_quantity",
                         [i.values() for i in test_data_dict.values()],
                         ids=[f"Test {i[0]} | String: '{i[1]['String']}' -> Result: {i[1]['Result']}"
                              for i in zip(test_data_dict.keys(), test_data_dict.values())]
                         )
def test_symbols_quantity_dict2(string, symbols_quantity):
    res = count_symbols_quantity_dict_shorter2(string)
    assert res == symbols_quantity, f"Test result {res} differs from expected result {symbols_quantity}"


@pytest.mark.parametrize("string, symbols, quantity",
                         [i.values() for i in test_data_list.values()],
                         ids=[f"Test {i[0]} | String: '{i[1]['String']}' -> "
                              f"Symbols: {i[1]['Symbols']}, Quantity: {i[1]['Quantity']}"
                              for i in zip(test_data_list.keys(), test_data_list.values())]
                         )
def test_symbols_quantity_list(string, symbols, quantity):
    # print_symbols_quantity_list(symbols, quantity)
    # assert (symbols, quantity) == count_symbols_quantity_list(string)
    s, q = count_symbols_quantity_list(string)
    assert s == symbols and q == quantity, f"Test result {s, q} differs from expected result {symbols, quantity}"
