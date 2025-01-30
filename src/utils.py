import json
import logging
import os
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion_function_eur, currency_conversion_function_usd

current_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir, "..", "logs", "utils.log")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions(file_path: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях
    """
    try:
        logger.info(f"Открытие файла{file_path}")
        with open(file_path, encoding="utf-8") as trans_file:
            transactions_file = json.load(trans_file)
            if type(transactions_file) is list and transactions_file is not False:
                logger.info("Словарь доступен")
                return transactions_file
            else:
                logger.warning("Формат данных не соответствует словарю")
                return []
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return []
    except JSONDecodeError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return []


def get_transaction_sum(transaction: dict) -> Any:
    """
    Функция принимает на вход транзакцию и возвращает ее сумму в рублях,
    если транзакция осуществлялась в долларах или евро, функция конвертирует
    сумму транзакции в рубли по текущему курсу, через api.apilayer.com
    """
    try:

        path_to_currency_code = transaction["operationAmount"]["currency"]["code"]
        if path_to_currency_code == "RUB":
            logger.info("Транзакция осуществлялась в рублях")
            result_rub = float(transaction["operationAmount"]["amount"])
            return result_rub

        if path_to_currency_code == "USD":
            logger.info("Транзакция осуществлялась в долларах")
            result_usd = float(transaction["operationAmount"]["amount"])
            usd_exchange_rate = currency_conversion_function_usd()
            result_from_usd_in_rub = result_usd * usd_exchange_rate
            return round(result_from_usd_in_rub, 2)

        if path_to_currency_code == "EUR":
            logger.info("Транзакция осуществлялась в евро")
            result_eur = float(transaction["operationAmount"]["amount"])
            eur_exchange_rate = currency_conversion_function_eur()
            result_from_eur_in_rub = result_eur * eur_exchange_rate
            return round(result_from_eur_in_rub, 2)
        else:
            logger.warning("Валюта в транзакции не соответствует искомой")
            return "No transactions were made in this currency"

    except KeyError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return "Transaction missing"
    except TypeError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return "Unable to determine the exchange rate of the specified currency"
