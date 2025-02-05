import datetime


def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Принимает список словарей и возвращает список словарей с заданным ключом"""
    new_list_dict = list()
    for _dict in list_dict:
        for value in _dict.values():
            if value == state:
                new_list_dict.append(_dict)
    return new_list_dict


def sort_by_date(list_dict_date: list, sort_order: bool = True) -> list:
    """Принимает список словарей и сортирует по ключу: 'date'"""
    return sorted(list_dict_date, key=lambda x: x["date"], reverse=sort_order)

def sort_by_sum_of_operation(list_dict_date: list, sort_order: bool = True) -> list:
    """Принимает список словарей и сортирует по ключу: 'amount'"""
    return sorted(list_dict_date, key=lambda x: x["operationAmount"]["amount"], reverse=sort_order)

def sort_by_code(list_dict_date: list, sort_order: bool = True) -> list:
    """Принимает список словарей и сортирует по ключу: 'code'"""
    return sorted(list_dict_date, key=lambda x: x["operationAmount"]["currency"]["code"] == "RUB", reverse=sort_order)

def date_changing(date: str) -> str:
    """Принимает дату и изменяет ее под нужный формат"""
    changing_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return changing_date

