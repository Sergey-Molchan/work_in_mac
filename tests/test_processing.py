from typing import Dict
from datetime import datetime
import pytest
from pythonproject.processing import filter_by_state, sort_by_date

@pytest.fixture
def test_transactions() -> list[dict]:
    """Фикстура с тестовыми транзакциями."""
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T00:00:00.000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-01-01T00:00:00.000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-06-15T00:00:00.000'},
        {'id': 4},  # Транзакция без статуса и даты
    ]


def test_filter_by_state(test_transactions):
    """Тест фильтрации по статусу."""
    result = filter_by_state(test_transactions)
    assert len(result) == 2
    assert all(t['state'] == 'EXECUTED' for t in result)


def test_sort_by_date(test_transactions):
    """Тест сортировки по дате."""
    result = sort_by_date(test_transactions)
    assert result[0]['id'] == 2  # Самая свежая транзакция


def get_date_key(x: Dict[str, str | int]) -> datetime:
    date_str = x.get('date', '')
    try:
        return datetime.fromisoformat(date_str.replace('Z', ''))
    except (ValueError, AttributeError):
        return datetime.min
