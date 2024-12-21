import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number() -> str:
    return "1234123412341234"


@pytest.fixture
def account_number() -> str:
    return "73654108430135874305"


def test_masks_card_number(card_number: str):
    assert get_mask_card_number(card_number) == "1234 12** **** 1234"
    assert get_mask_card_number("1234") == "1234 **** ** "
    assert get_mask_card_number("") == "**** **  "


def test_masks_account_number(account_number: str):
    assert get_mask_account(account_number) == "**4305"
    assert get_mask_account("") == "****"
    assert get_mask_account("123") == "***123"
