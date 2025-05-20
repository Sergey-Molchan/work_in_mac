from datetime import datetime
from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Фильтрует транзакции по статусу."""
    return [t for t in transactions if t.get('state') == state]


def sort_by_date(transactions: List[Dict[str, str | int]], reverse: bool = True) -> List[Dict]:
    """Сортирует транзакции по дате."""

    def get_date_key(x: Dict[str, str | int]) -> datetime:
        date_str = x.get('date', '')
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f") if date_str else datetime.min
        except ValueError:
            return datetime.min

    return sorted(transactions, key=get_date_key, reverse=reverse)
