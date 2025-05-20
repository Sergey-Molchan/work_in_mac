from pythonproject.masks import mask_card, mask_account
import pytest


@pytest.mark.parametrize("input_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("7000792289606361", "7000 79** **** 6361"),
    ("1111222233334444", "1111 22** **** 4444"),
])
def test_mask_card(input_number, expected):
    assert mask_card(input_number) == expected


@pytest.mark.parametrize("input_number, expected", [
    ("73654108430135874305", "**4305"),
    ("98765432109876543210", "**3210"),
    ("12345678901234567890", "**7890"),
])
def test_mask_account(input_number, expected):
    assert mask_account(input_number) == expected


@pytest.mark.parametrize("invalid_input", [
    "123456789012345",  # 15 digits
    "12345678901234567",  # 17 digits
    "123456789012345a",  # contains letter
    "",  # empty string
])
def test_mask_card_invalid(invalid_input):
    with pytest.raises(ValueError):
        mask_card(invalid_input)


@pytest.mark.parametrize("invalid_input", [
    "123",  # less than 4 digits
    "123a",  # contains letter
    "",  # empty string
])
def test_mask_account_invalid(invalid_input):
    with pytest.raises(ValueError):
        mask_account(invalid_input)
