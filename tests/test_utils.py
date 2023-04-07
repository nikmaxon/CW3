import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formated_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data, filtered_empty_from=False)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 3


def test_get_last_values(test_data):
    data = get_last_values(test_data, 2)
    expected_data = [{
        "id": 441945886,
        "state": "CANCELED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }, ]
    assert data == expected_data


def test_get_formated_data(test_data):
    data = get_formated_data(test_data)
    expected_data = [
        '\n2019-08-26 10:50:58.294041 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.',
        '\n2019-07-03 18:35:29.512364 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD',
        '\n2018-06-30 02:08:58.425572 Перевод организации\nСчет 7510 68** **** 6952 -> Счет **6702\n9824.07 USD',
        '\n2018-03-23 10:45:06.972075 Открытие вклада\nСчет скрыт  -> Счет **2431\n48223.05 руб.',
        '\n2019-04-04 23:20:05.206878 Перевод со счета на счет\nСчет 1970 86** **** 8542 -> Счет **4188\n79114.93 USD']
    assert data == expected_data
