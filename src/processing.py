def filter_by_state(list_dict: list, state="EXECUTED") -> list:
    """Принимает список словарей и возвращает список словарей с заданным ключом"""
    new_list_dict = []
    for _dict in new_list_dict:
        for key in _dict.keys():
            if key == state:
                new_list_dict.append(_dict)
    return new_list_dict


def sort_by_date(list_dict_date: list, status=True) -> list:
    """Принимает список словарей и сортирует по ключу: 'date'"""
    return sorted(list_dict_date, key=lambda x: x["date"], reverse=status)
