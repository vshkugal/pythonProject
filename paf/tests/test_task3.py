import pytest
from paf.src.paf8_task3 import my_range
import numpy as np

test_data_1 = {"1": 10, "2": -10, "3": 10.0, "4": 1000000, "5": 0}

test_data_2 = {
    "1":
        {"Start": 0, "Stop": 10},
    "2":
        {"Start": 5, "Stop": 10},
    "3":
        {"Start": 30, "Stop": 2},
    "4":
        {"Start": 5.5, "Stop": 10.5},
    "5":
        {"Start": -10, "Stop": 10}
}

test_data_3 = {
    "1":
        {"Start": 0, "Stop": 10, "Step": 1},
    "2":
        {"Start": 5, "Stop": 15, "Step": 2},
    "3":
        {"Start": 0.5, "Stop": 10.5, "Step": 1.5},
    "4":
        {"Start": -10, "Stop": 0, "Step": 1},
    "5":
        {"Start": -5.0, "Stop": 5.0, "Step": 0.5},
    "6":
        {"Start": 0, "Stop": -10, "Step": -1},
    "7":
        {"Start": 5, "Stop": -5, "Step": -1.5},
    "8":
        {"Start": 8, "Stop": 2, "Step": -3},
    "9":
        {"Start": 10, "Stop": 0, "Step": 1},
    "10":
        {"Start": 5.1, "Stop": -1.3, "Step": -1.1}
}


@pytest.mark.parametrize("stop_number",
                         [i for i in test_data_1.values()],
                         ids=[f"Test {i[1]} with 1 arg | End: {i[0]}"
                              for i in zip(test_data_1.values(), test_data_1.keys())]
                         )
def test_my_range_1(stop_number):
    assert [i for i in my_range(stop_number)] == [i for i in np.arange(stop_number)], \
        "The range functions' results are different"


@pytest.mark.parametrize("start_number2, stop_number2",
                         [i.values() for i in test_data_2.values()],
                         ids=[f"Test {i[1]} with 2 args | Start: {i[0]['Start']}, End: {i[0]['Stop']}"
                              for i in zip(test_data_2.values(), test_data_2.keys())]
                         )
def test_my_range_2(start_number2, stop_number2):
    assert [i for i in my_range(start_number2, stop_number2)] == \
           [i for i in np.arange(start_number2, stop_number2)], \
           "The range functions' results are different"


@pytest.mark.parametrize("start_number3, stop_number3, step3",
                         [i.values() for i in test_data_3.values()],
                         ids=[
                             f"Test {i[1]} with 3 args | "
                             f"Start: {i[0]['Start']}, End: {i[0]['Stop']}, Step: {i[0]['Step']}"
                             for i in zip(test_data_3.values(), test_data_3.keys())]
                         )
def test_my_range_3(start_number3, stop_number3, step3):
    assert [i for i in my_range(start_number3, stop_number3, step3)] == \
           [i for i in np.arange(start_number3, stop_number3, step3)], \
           "The range functions' results are different"
