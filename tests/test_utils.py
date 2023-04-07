import pytest

from utils import get_data, get_filtered_data, get_last_values


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data, filtered_empty_from=False)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 3


def test_get_last_values(test_data):
    data = get_last_values(test_data, 2)
    print(x['date'] for x in data)
