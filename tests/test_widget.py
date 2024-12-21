import pytest
from src.widget import mask_account_card, get_date



@pytest.mark.parametrize("testing_string, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("", "**** **** **** ")
])
def test_widget_mask_card(testing_string, expected):
    assert mask_account_card(testing_string) == expected


@pytest.mark.parametrize("testing_list, date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("", ".."),
    ("32412151234", "23.15.3241")
])
def test_widget_date(testing_list, date):
    assert get_date(testing_list) == date
