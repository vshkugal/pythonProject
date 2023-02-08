import pytest
from paf.src.paf8_task3 import my_range
import numpy as np


check_lib = np.arange
single_data = {
    "single arg 1": {"data": (10,), "check_lib": check_lib},
    "single arg 2": {"data": (-10,), "check_lib": check_lib},
    "single arg 3": {"data": (10.0,), "check_lib": check_lib},
    "single arg 4": {"data": (1000000,), "check_lib": check_lib},
    "single arg 5": {"data": (0,), "check_lib": check_lib},
    "two args 1": {"data": (0,), "check_lib": check_lib},
    "two args 2": {"data": (5, 10), "check_lib": check_lib},
    "two args 3": {"data": (30, 2), "check_lib": check_lib},
    "two args 4": {"data": (5.5, 10.5), "check_lib": check_lib},
    "two args 5": {"data": (-10, 10), "check_lib": check_lib},
    "three args 1": {"data": (0, 10, 1), "check_lib": check_lib},
    "three args 2": {"data": (5, 15, 2), "check_lib": check_lib},
    "three args 3": {"data": (0.5, 10.5, 1.5), "check_lib": check_lib},
    "three args 4": {"data": (-10, 0, 1), "check_lib": check_lib},
    "three args 5": {"data": (-5.0, 5.0, 0.5), "check_lib": check_lib},
    "three args 6": {"data": (0, -10, -1), "check_lib": check_lib},
    "three args 7": {"data": (5, -5,  -1.5), "check_lib": check_lib},
    "three args 8": {"data": (8, 2, -3), "check_lib": check_lib},
    "three args 9": {"data": (10, 0, 1), "check_lib": check_lib},
}


@pytest.mark.parametrize("test_data, check_lib",
                         [i.values() for i in single_data.values()],
                         ids=[
                             f"Test with {i[1]} "
                             f"Params: {i[0]['data']}, check_lib: {i[0]['check_lib'].__name__}"
                             for i in zip(single_data.values(), single_data.keys())]
                         )
def test_my_range_3(test_data, check_lib):
    assert [i for i in my_range(*test_data)] == \
           [i for i in check_lib(*test_data)], \
           "The range functions' results are different"
