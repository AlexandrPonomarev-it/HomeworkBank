import json
import unittest
from unittest.mock import mock_open, patch
from src.utils import get_financial_transactions, get_transaction_sum


class TestReadJsonFile(unittest.TestCase):
    def test_get_financial_transactions(self):
        mock_data = '[{"id": 1, "amount": 100}]'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = get_financial_transactions('test_file.json')
            self.assertEqual(result, [{"id": 1, "amount": 100}])

    def test_read_json_file_empty(self):
        with patch('builtins.open', mock_open(read_data='')):
            result = get_financial_transactions('fake_path.json')
            self.assertEqual(result, [])



class TestGetTransactionSumUsd(unittest.TestCase):
    @patch('requests.get')
    def test_get_transaction_sum(self, mock_get):
        # Задаем фиктивный ответ API
        mock_response = {
            "rates": {
                "RUB": 95.0
            },
            "base": "USD"
        }
        mock_get.return_value.text = json.dumps(mock_response)

        # Вызываем функцию и проверяем результат
        result = get_transaction_sum({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "1",
      "currency": {
        "name": "USD",
        "code": "USD"
      }}})
        self.assertEqual(result, 95.0)


class TestGetTransactionSumEur(unittest.TestCase):
    @patch('requests.get')
    def test_get_transaction_sum(self, mock_get):
        # Задаем фиктивный ответ API
        mock_response = {
            "rates": {
                "RUB": 100.0
            },
            "base": "EUR"
        }
        mock_get.return_value.text = json.dumps(mock_response)

        # Вызываем функцию и проверяем результат
        result = get_transaction_sum({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "1",
      "currency": {
        "name": "EUR",
        "code": "EUR"
      }}})
        self.assertEqual(result, 100.0)


def test_get_transaction_sum_rub():
    assert get_transaction_sum({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }}}) == 31957.58

def test_get_transaction_sum_no_currency():
    assert get_transaction_sum({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "GBR"
      }}}) == "No transactions were made in this currency"

def test_get_transaction_sum_no_code():
    assert get_transaction_sum({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "cod": "GBR"
      }}}) == "Transaction missing"

def test_get_transaction_sum_no_type():
    assert get_transaction_sum([{}]) == "Unable to determine the exchange rate of the specified currency"
