import unittest
from unittest.mock import patch

import pandas as pd

from src.open_csv_excel_file import read_excel_file


class TestReadExcelFile(unittest.TestCase):
    def test_valid_data(self):
        mock_data = pd.DataFrame({
            'id': [1],
            'state': ['EXECUTED'],
            'date': ['2023-09-05T11:30:32Z'],
            'amount': [16210],
            'currency_name': ['Sol'],
            'currency_code': ['PEN'],
            'from': ['Счет 58803664561298323391'],
            'to': ['Счет 39745660563456619397'],
            'description': ['Перевод организации']
        })
        with patch('pandas.read_excel', return_value=mock_data):
            result = read_excel_file('dummy.xlsx')
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]['id'], 1)

    def test_file_not_found(self):
        with patch('pandas.read_excel', side_effect=FileNotFoundError):
            result = read_excel_file('dummy.xlsx')
            self.assertEqual(result, "Файл не найден")

    def test_invalid_data(self):
        with patch('pandas.read_excel', side_effect=ValueError):
            result = read_excel_file('dummy.xlsx')
            self.assertEqual(result, "Дынные в файле отсутствуют или не соответствуют формату")