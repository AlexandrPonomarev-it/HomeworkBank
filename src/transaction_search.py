import re
from collections import Counter
from typing import Any


def search_for_a_transaction_by_keyword(operations_list: Any, search_string: str) -> Any:
    """Функция принимает список словарей с данными о
    банковских операциях и строку поиска, и возвращает список словарей,
    у которых в описании есть данная строка"""

    try:
        pattern = re.compile("description")
        result_searching_list = []
        for operations in operations_list:
            for key, values in operations.items():
                if re.search(pattern, key) and search_string.lower() in values.lower():
                    result_searching_list.append(operations)
        return result_searching_list
    except AttributeError:
        return "Введены некорректные данные"


def number_of_transactions(transactions_list: list, category_list: list) -> Any:
    """Функция принимает список транзаций и категорий операций, а возвращает
    словарь с количеством транзакций по каждой категории"""

    try:
        description_list = []
        for operations in transactions_list:
            if operations["description"] in category_list:
                description_list.append(operations["description"])
        operation_counter = Counter(description_list)
        return dict(operation_counter)
    except TypeError:
        return "Входящие данные не верны"
