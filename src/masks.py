def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает номер банковской карты и возвращает замаскированный номер,
    в котором цифры с 9 по 14 заменены на *
    """
    str_card_number = str(card_number)
    mask_card_number = str_card_number[0:6] + "******" + str_card_number[12:16]

    return f"{mask_card_number[0:4]} {mask_card_number[4:8]} {mask_card_number[8:12]} {mask_card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает номер банковского счета и возвращает замаскированный счет,
    в котором показаны последние 4 цифры, а перед ними стоят две *
    """
    str_account_number = str(account_number)
    mask_account_number = "**" + str_account_number[-4:]

    return f"{mask_account_number[0:2]}{mask_account_number[-4:]}"
