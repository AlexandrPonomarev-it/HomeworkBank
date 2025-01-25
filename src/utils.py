import json
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion_function_eur, currency_conversion_function_usd


def get_financial_transactions(file_path: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях
    """
    try:
        with open(file_path, encoding="utf-8") as trans_file:
            transactions_file = json.load(trans_file)
            if type(transactions_file) is list and transactions_file is not False:
                return transactions_file
            else:
                return []
    except FileNotFoundError:
        return []
    except JSONDecodeError:
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
            result_rub = float(transaction["operationAmount"]["amount"])
            return result_rub

        if path_to_currency_code == "USD":
            result_usd = float(transaction["operationAmount"]["amount"])
            usd_exchange_rate = currency_conversion_function_usd()
            result_from_usd_in_rub = result_usd * usd_exchange_rate
            return round(result_from_usd_in_rub, 2)

        if path_to_currency_code == "EUR":
            result_eur = float(transaction["operationAmount"]["amount"])
            eur_exchange_rate = currency_conversion_function_eur()
            result_from_eur_in_rub = result_eur * eur_exchange_rate
            return round(result_from_eur_in_rub, 2)
        else:
            return "No transactions were made in this currency"

    except KeyError:
        return "Transaction missing"
    except TypeError:
        return "Unable to determine the exchange rate of the specified currency"
