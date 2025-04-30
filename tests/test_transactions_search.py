import unittest

import pytest

from src.transaction_search import search_for_a_transaction_by_keyword, number_of_transactions


class TestSearchFunction(unittest.TestCase):
    def test_search_for_a_transaction_by_keyword(self):
        operations_list = [
            {"description": "Оплата услуг", "amount": 100},
            {"description": "Перевод на карту", "amount": 200},
            {"description": "Покупка в магазине", "amount": 300},
        ]
        search_string = "Перевод"
        expected_result = [{"description": "Перевод на карту", "amount": 200}]
        result = search_for_a_transaction_by_keyword(operations_list, search_string)
        self.assertEqual(result, expected_result)

    def test_incorrect_data(self):
        operations_list = "Некорректные данные"
        search_string = "Перевод"
        expected_result = "Введены некорректные данные"
        result = search_for_a_transaction_by_keyword(operations_list, search_string)
        self.assertEqual(result, expected_result)


transactions_list = [
    {"description": "Покупка в магазине"},
    {"description": "Перевод на карту"},
    {"description": "Покупка в магазине"},
    {"description": "Оплата услуг"},
]

category_list = ["Покупка в магазине", "Перевод на карту", "Оплата услуг"]

expected_result_trans = {"Покупка в магазине": 2, "Перевод на карту": 1, "Оплата услуг": 1}


@pytest.mark.parametrize(
    "operations, categories, expected",
    [(transactions_list, category_list, expected_result_trans), ([], category_list, {}), (transactions_list, [], {})],
)
def test_number_of_transactions(operations, categories, expected):
    assert number_of_transactions(operations, categories) == expected
