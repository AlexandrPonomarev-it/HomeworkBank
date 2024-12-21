import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def card_number():
    return "1234123412341234"

@pytest.fixture
def account_number():
    return "73654108430135874305"



def test_masks_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 12** **** 1234"


def test_masks_account_number(account_number):
    assert get_mask_account(account_number) == "**4305"