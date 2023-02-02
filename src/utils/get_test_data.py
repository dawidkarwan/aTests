import json
import logging
from typing import TypeVar, Type
from pathlib import PurePath
from dacite import from_dict

ROOT = PurePath(__file__).parent.parent.parent
TEST_PATH = ROOT / 'tests'
TEST_DATA_PATH = TEST_PATH / 'data'

T = TypeVar('T')


def load_json(file_path: PurePath | str) -> dict:
    with open(file_path, encoding='utf-8') as json_file:
        return json.load(json_file)


def get_test_data(suite_name: str, data_class: Type[T]) -> list[T]:
    file_path = TEST_DATA_PATH / f'{suite_name}_test_data.json'
    try:
        return [from_dict(data_class=data_class, data=data) for data in load_json(file_path)]
    except FileNotFoundError:
        logging.warning(f'no file for path: {file_path}')
        return []
