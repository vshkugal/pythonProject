"""PAF-2: Data format validation
Написать тест для проверки данных в файлах, содержащих дату, соответствие формату
(данные валидны и записаны в формате “dd.mm.yyyy”).
Данные в файлах отделены друг от друга символом: “;”.
Имена файлов записываются в список или записаны в файл.
Пример: [“data.txt”, “data2.txt”, “data3.txt”].
"""
from typing import List


def read_file(file_name: str) -> List[str]:
    """
    Read from file
    :param file_name: str
    :return: List[str]
    """
    with open(file_name) as f:
        read_data = f.read()
        data_list = read_data.split(';')
        return data_list
