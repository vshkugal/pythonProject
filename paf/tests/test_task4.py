import os
from pathlib import Path
import pytest
import re
from paf.src.paf2_task4 import read_file

date_regex = re.compile(r'\d\d\.\d\d\.\d\d\d\d')
file_path = r'../data'
# file_names = ["data.txt", "data2.txt", "data3.txt", "data4.txt"]
# file_names = list((Path(file_path)).glob('*'))
# file_names = list((Path(file_path)).glob('data*.txt'))
file_names = os.listdir(file_path)

# ----------------------------------------------
# Test the whole files using parametrization
# ----------------------------------------------


@pytest.mark.parametrize("file_name", file_names,
                         ids=[f"Test {i+1} with file {file_names[i]}" for i in range(len(file_names))]
                         )
def test_date_format(file_name):
    data_list = read_file(Path(file_path, file_name))
    invalid_list = []
    for i in range(len(data_list)):
        mo = date_regex.search(data_list[i])
        if not mo or mo.group() != data_list[i]:
            invalid_list.append(data_list[i])
    assert invalid_list == [], f'{invalid_list} from {file_name} are not valid dates'
