import unittest
from unittest.mock import mock_open
from unittest.mock import patch
from src.open_csv_excel_file import read_csv_file





class TestReadCSVFile(unittest.TestCase):
    def test_valid_data(self):
        """ Проверка нормальных условий работы функции """
        mock_data = ("id;state;date;amount;currency_name;currency_code;from;to;description\n1;"
                     "EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;"
                     "Счет 39745660563456619397;Перевод организации")
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = read_csv_file('dummy.csv')
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]['id'], '1')

    def test_file_not_found(self):
        """ Проверка работы функции с отсутствующим файлом """
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = read_csv_file('dummy.csv')
            self.assertEqual(result, "Файл не найден")

    def test_empty_file(self):
        """ Проверка работы функции с пустым файлом """
        with patch('builtins.open', mock_open(read_data="")):
            result = read_csv_file('dummy.csv')
            self.assertEqual(result, [])

