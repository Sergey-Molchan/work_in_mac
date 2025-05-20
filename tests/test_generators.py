from typing import List, Dict
import pytest
from pythonproject.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Остальной код остаётся без изменений


@pytest.fixture
def test_transactions() -> List[Dict]:
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Payment"},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}, "description": "Transfer"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Withdrawal"},
    ]


@pytest.mark.parametrize("currency, expected_ids", [("USD", [1, 3]), ("EUR", [2])])
def test_filter_by_currency(test_transactions, currency, expected_ids):
    result = list(filter_by_currency(test_transactions, currency))
    assert [t["id"] for t in result] == expected_ids


def test_transaction_descriptions(test_transactions):
    descriptions = list(transaction_descriptions(test_transactions))
    assert descriptions == ["Payment", "Transfer", "Withdrawal"]


@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
])
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected
