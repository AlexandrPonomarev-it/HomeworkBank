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


def test_get_transaction_sum():
    assert get_transaction_sum(  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }}}) == 31957.58
    assert get_transaction_sum({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }}}) == 803320.7
    assert get_transaction_sum({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "5431.23",
      "currency": {
        "name": "EUR",
        "code": "EUR"
      }}}) == 557420.6
    assert get_transaction_sum({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "1234.32",
      "currency": {
        "name": "GBP",
        "code": "GBP"
      }}}) == "No transactions were made in this currency"
    assert get_transaction_sum({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "1234.32",
      "currency": {
        "name": "GBP",
        "cod": "GBP"
      }}}) == "Transaction missing"
    assert get_transaction_sum({"sdfasdf"}) == "Unable to determine the exchange rate of the specified currency"