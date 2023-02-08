import pytest
from paf.src.paf4_task1 import find_pairs

my_list = [1, 12, 5, 7, 3, 875, 343, 8, 43, 56, 6, 2, 10, 54]


def id_string(input_string):
    string_list = str(input_string)
    if string_list.isdecimal():
        return f' Sum {string_list} '
    else:
        return f' List {string_list} '


@pytest.mark.parametrize("input_list, input_sum, result_list",
                         [(my_list, 15, [[12, 3], [5, 10], [7, 8]]),
                          (my_list, 64, [[8, 56], [10, 54]]),
                          (my_list, 10, [[7, 3], [8, 2]]),
                          (my_list, 77, []),
                          ([1, 12], 13, [[1, 12]]),
                          ([1, 12], 5, []),
                          ([1], 2, []),
                          ([], 0, [])
                          ], ids=id_string
                         )
def test_find_pair(input_list, input_sum, result_list):
    assert find_pairs(input_list, input_sum) == result_list

# pytest test_task1.py -v
