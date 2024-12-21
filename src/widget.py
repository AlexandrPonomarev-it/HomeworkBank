import re

from src.masks import get_mask_account, get_mask_card_number


def is_english(list_letter: str) -> bool:
    """Проверяет на вхождение английских букв"""
    return bool(re.search("[a-zA-z]", list_letter))


def is_russian(list_letter: str) -> bool:
    """Проверяет на вхождение русских букв"""
    return bool(re.search("[а-яА-Я]", list_letter))


def mask_account_card(card_info: str) -> str:
    """Функция принимает номер карты или счета и возвращает замаскированную строку"""
    card_account_letter = ""
    card_account_number = ""
    if is_russian(card_info):
        return f"Счет {get_mask_account(card_info)}"

    for num in card_info:
        if is_english(num) or num == " ":
            card_account_letter += num
        if num.isdigit():
            card_account_number += num

    mask_card_account_number = card_account_number[0:6] + "******" + card_account_number[12:16]
    return f"{card_account_letter}{get_mask_card_number(mask_card_account_number)}"


def get_date(data_str: str) -> str:
    """Функция принимает строку с датой и возвращает измененную дату"""
    clear_data = ""
    clear_data += data_str[8:10] + "." + data_str[5:7] + "." + data_str[0:4]
    return clear_data
