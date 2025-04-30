import unittest
from unittest.mock import patch
from src.external_api import currency_conversion_function_usd, currency_conversion_function_eur
import json


class TestCurrencyConversionFunctionUsd(unittest.TestCase):
    @patch('requests.get')
    def test_currency_conversion_function_usd(self, mock_get):
        # Задаем фиктивный ответ API
        mock_response = {
            "rates": {
                "RUB": 95.0
            },
            "base": "USD"
        }
        mock_get.return_value.text = json.dumps(mock_response)

        # Вызываем функцию и проверяем результат
        result = currency_conversion_function_usd()
        self.assertEqual(result, 95.0)


class TestCurrencyConversionFunctionEur(unittest.TestCase):
    @patch('requests.get')
    def test_currency_conversion_function_eur(self, mock_get):
        # Задаем фиктивный ответ API
        mock_response = {
            "rates": {
                "RUB": 100.0
            },
            "base": "EUR"
        }
        mock_get.return_value.text = json.dumps(mock_response)

        # Вызываем функцию и проверяем результат
        result = currency_conversion_function_eur()
        self.assertEqual(result, 100.0)
