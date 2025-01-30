import csv
from typing import Any
import pandas as pd
from pandas.core.methods.to_dict import to_dict

path_to_csv_file = "../transactions.csv"
path_to_excel_file = "../transactions_excel.xlsx"


def read_csv_file(csv_file: Any) -> Any:
    """Функция для считывания финансовых операций из CSV"""
    try:
        with open(csv_file) as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        return "Файл не найден"


def read_excel_file(excel_file: Any) -> Any:
    """Функция для считывания финансовых операций из excel"""
    try:
        df_excel = pd.read_excel(excel_file)
        list_transaction_excel = list(to_dict(df_excel, orient="records"))

        return list_transaction_excel
    except ValueError:
        return "Дынные в файле отсутствуют или не соответствуют формату"
    except FileNotFoundError:
        return "Файл не найден"


