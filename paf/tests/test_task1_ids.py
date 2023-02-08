import pytest
from paf.src.paf4_task1 import find_pairs

my_list = [1, 12, 5, 7, 3, 875, 343, 8, 43, 56, 6, 2, 10, 54]

test_data = {
    "Normal test 1":
        {"Test data": my_list, "Sum": 15, "Result": [[12, 3], [5, 10], [7, 8]]},
    "Normal test 2":
        {"Test data": my_list, "Sum": 64, "Result": [[8, 56], [10, 54]]},
    "Normal test 3":
        {"Test data": my_list, "Sum": 10, "Result": [[7, 3], [8, 2]]},
    "Empty result 1":
        {"Test data": my_list, "Sum": 77, "Result": []},
    "Normal test 4":
        {"Test data": [1, 12], "Sum": 13, "Result": [[1, 12]]},
    "Empty result 2":
        {"Test data": [1, 12], "Sum": 5, "Result": []},
    "Empty result 3":
        {"Test data": [1], "Sum": 2, "Result": []},
    "Empty result 4":
        {"Test data": [], "Sum": 0, "Result": []}
}


@pytest.mark.parametrize("input_list, input_sum, result_list",
                         [i.values() for i in test_data.values()],
                         ids=[f"{i[1]} | Input list: {i[0]['Test data']}, Sum: {i[0]['Sum']}, Result: {i[0]['Result']}"
                              for i in zip(test_data.values(), test_data.keys())]
                         )
def test_find_pair(input_list, input_sum, result_list):
    assert find_pairs(input_list, input_sum) == result_list, "The test failed"

# pytest test_task1_ids.py -v
