import os
from pathlib import Path
import pytest
import re

file_path = r'../data'
# file_names = ["data.txt", "data2.txt", "data3.txt", "data4.txt"]
# file_names = list((Path(file_path)).glob('*'))
# file_names = list((Path(file_path)).glob('data*.txt'))
file_names = os.listdir(file_path)
separator = ';'
date_regex = re.compile(r'\d\d\.\d\d\.\d\d\d\d')


# -------------------------------------------------
# Test the whole files using fixtures
# -------------------------------------------------


@pytest.fixture(scope="function", params=file_names,
                ids=[f"Test {i+1} with file {file_names[i]}" for i in range(len(file_names))])
def read_file(request):
    with open(Path(file_path, request.param)) as f:
        read_data = f.read()
        data_list = read_data.split(separator)
        yield data_list


def test_date_format_file(read_file):
    invalid_list = []
    for i in range(len(read_file)):
        mo = date_regex.search(read_file[i])
        if not mo or mo.group() != read_file[i]:
            invalid_list.append(read_file[i])
    assert invalid_list == [], f'{invalid_list} are not valid dates'


# -------------------------------------------------
# Test the files line-by-line using fixtures
# -------------------------------------------------


def read_file_lines():
    for file_name in file_names:
        with open(Path(file_path, file_name)) as f:
            read_data = f.read()
            data_list = read_data.split(separator)
            for data_line in data_list:
                yield file_name, data_line


@pytest.fixture(scope="function", params=read_file_lines(),
                ids=[f"Test line {i[1]} in file {i[0]}" for i in read_file_lines()])
def read_lines(request):
    yield request.param


def test_date_format_lines(read_lines):
    mo = date_regex.search(read_lines[1])
    message = f'{read_lines[1]} in {read_lines[0]} is not a valid date'
    # assert mo is not None and mo.group() == read_lines[1], message
    if not mo:
        raise ValueError(message)
    assert mo.group() == read_lines[1], message


# -------------------------------------------------
# Test the files line-by-line using parametrization
# -------------------------------------------------


@pytest.mark.parametrize("file_name, data_line", read_file_lines(),
                         ids=[f"Test line {i[1]} in file {i[0]}" for i in read_file_lines()])
def test_date_format_lines_2(file_name, data_line):
    mo = date_regex.search(data_line)
    message = f'{data_line} in {file_name} is not a valid date'
    assert mo is not None and mo.group() == data_line, message
    """if not mo:
        raise ValueError(message)
    assert mo.group() == data_line, message"""
