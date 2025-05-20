import pytest


@pytest.fixture
def test_card_numbers() -> list[str]:
    return ["1234567890123456", "7000792289606361"]


@pytest.fixture
def test_account_numbers() -> list[str]:
    return ["73654108430135874305", "98765432109876543210"]


@pytest.fixture
def test_transactions() -> list[dict]:
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T00:00:00.000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-01-01T00:00:00.000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-06-15T00:00:00.000'},
        {'id': 4},  # Транзакция без статуса и даты
    ]
