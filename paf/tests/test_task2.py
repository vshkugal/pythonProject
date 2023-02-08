import pytest
from paf.src.paf7_task2 import weight_capacity


test_data = {
    "1":
        {"Packs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Days": 5, "Weight capacity": 15},
    "2":
        {"Packs": [3, 2, 2, 4, 1, 4], "Days": 3, "Weight capacity": 6},
    "3":
        {"Packs": [1, 2, 3, 1, 1], "Days": 4, "Weight capacity": 3},
    "4":
        {"Packs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Days": 6, "Weight capacity": 11},
    "5":
        {"Packs": [3, 2, 2, 4, 1, 4], "Days": 2, "Weight capacity": 9},
    "6":
        {"Packs": [1, 2, 3, 1, 1], "Days": 3, "Weight capacity": 3},
    "7":
        {"Packs": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "Days": 5, "Weight capacity": 15},
    "8":
        {"Packs": [14, 4, 5, 16, 2, 21, 1, 19], "Days": 5, "Weight capacity": 21},
    "9":
        {"Packs": [14, 4, 5, 16, 2, 21, 1, 19], "Days": 5, "Weight capacity": 7}
}


@pytest.mark.parametrize("my_weights, my_days, result_capacity",
                         [i.values() for i in test_data.values()],
                         ids=[f"Test {i[1]} | Packs to load: {i[0]['Packs']}, Days: {i[0]['Days']} -> "
                              f"Weight capacity: {i[0]['Weight capacity']}"
                              for i in zip(test_data.values(), test_data.keys())]
                         )
def test_weight_capacity(my_weights, my_days, result_capacity):
    assert weight_capacity(my_weights, my_days) == result_capacity, \
        f"Test result {weight_capacity(my_weights, my_days)} differs from expected result {result_capacity}"

# pytest test_task2.py -v
