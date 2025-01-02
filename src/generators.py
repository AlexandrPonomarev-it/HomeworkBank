def filter_by_currency(list_dict_transaction: list, currency: str):
    """Функция принимает список транзакции и возвращает итератор,
    который поочередно выдает транзакции с валютой: 'USD'"""
    for trans in list_dict_transaction:
        for value in trans.values():
            if isinstance(value, dict):
                for val in value.values():
                    if isinstance(val, dict):
                        for k, v in val.items():
                            if k == "code" and v == currency:
                                yield trans


def transaction_descriptions(list_with_transactions: list):
    """Функция принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    for description in list_with_transactions:
        for key, value in description.items():
            if key == "description":
                yield value


def encoding_a_new_card(range_numbers: int) -> str:
    """Функция принимает генерируемый диапазон чисел
    и возвращает номер карты с принятым числом"""
    zero_card_number = "0000000000000000"
    str_range_numbers = str(range_numbers)
    new_string = zero_card_number[len(str_range_numbers) :] + str_range_numbers
    return new_string


def card_number_generator(a: int, b: int):
    """Функция принимает диапазон чисел и возвращает
    и генерирует номера карт в заданном диапазоне"""
    for i in range(a, b + 1):
        if a <= b:
            card_number_with_spaces = (
                f"{encoding_a_new_card(a)[:4]} {encoding_a_new_card(a)[4:8]} "
                f"{encoding_a_new_card(a)[8:12]} {encoding_a_new_card(a)[12:17]}"
            )
            yield card_number_with_spaces
            a += 1
