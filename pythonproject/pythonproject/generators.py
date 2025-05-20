from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """Фильтрует транзакции по валюте и возвращает итератор."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """Генератор описаний транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, stop + 1):
        num_str = f"{num:016d}"  # 16-значная строка с ведущими нулями
        formatted = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        yield formatted
