import json
import logging
from typing import Any

from dacite import from_dict

BASE_PATH = 'C:\\PyProjects\\aTests\\files\\'
SUFFIX_SUITE_NAME = '_test_data.json'


def load_json(file_path: str) -> dict:
    with open(file_path, encoding='utf-8') as json_file:
        return json.load(json_file)


def get_test_data(suite_name: str, data_class) -> list[Any]:
    file_path = BASE_PATH + suite_name + SUFFIX_SUITE_NAME
    test_data = []
    try:
        for data in load_json(file_path):
            test_data.append(from_dict(data_class=data_class, data=data))
        return test_data
    except FileNotFoundError:
        logging.error(f'no file for path: {file_path}')
        return []
