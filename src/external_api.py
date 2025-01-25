import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')



def currency_conversion_function_eur() -> Any:
    """
    Функция запрашивает и возвращает данные о курсе валюты EUR по отношению к RUB
    """
    api_url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=EUR"
    headers = {"apikey": api_key}

    response = requests.get(api_url, headers=headers)
    result = response.text
    dict_result = json.loads(result)

    return dict_result["rates"]["RUB"]


def currency_conversion_function_usd() -> Any:
    """
    Функция запрашивает и возвращает данные о курсе валюты USD по отношению к RUB
    """
    api_url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=USD"
    headers = {"apikey": api_key}

    response = requests.get(api_url, headers=headers)
    result = response.text
    dict_result = json.loads(result)

    return dict_result["rates"]["RUB"]

print(currency_conversion_function_usd())