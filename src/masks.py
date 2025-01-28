import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir, "..", "logs", "masks.log")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает номер банковской карты и возвращает замаскированный номер,
    в котором цифры с 9 по 14 заменены на *
    """
    try:
        logger.info("Получен номер карты")
        str_card_number = str(card_number)
        logger.info("Кодирование номера карты")
        mask_card_number = str_card_number[0:6] + "******" + str_card_number[12:16]

        return f"{mask_card_number[0:4]} {mask_card_number[4:8]} {mask_card_number[8:12]} {mask_card_number[12:]}"
    except NameError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return "Ведены некорректные данные"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает номер банковского счета и возвращает замаскированный счет,
    в котором показаны последние 4 цифры, а перед ними стоят две *
    """
    try:
        logger.info("Получен номер счета")
        str_account_number = str(account_number)
        logger.info("Кодирование номера счета")
        mask_account_number = "**" + str_account_number[-4:]

        return f"{mask_account_number[0:2]}{mask_account_number[-4:]}"

    except NameError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return "Ведены некорректные данные"
