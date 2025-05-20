from datetime import datetime
from typing import Optional
from pythonproject.masks import mask_card, mask_account  #Проверка работы git

def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.
    Примеры:
        "Visa Platinum 7000792289606361" → "Visa Platinum 7000 79** **** 6361"
        "Счет 73654108430135874305" → "Счет **4305"
    """
    if not data or not isinstance(data, str):
        raise ValueError("Некорректные входные данные")

    parts = data.split()
    if len(parts) < 2:
        raise ValueError("Неверный формат данных")

    number = parts[-1]

    if "счет" in data.lower():
        return f"{' '.join(parts[:-1])} {mask_account(number)}"  # Используем mask_account
    return f"{' '.join(parts[:-1])} {mask_card(number)}"



def get_date(raw_date: str) -> Optional[str]:
    """Преобразует дату из формата ISO в DD.MM.YYYY"""
    try:
        date_obj = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return None


def main():
    """Точка входа в приложение"""
    test_cards = [
        "Visa Platinum 7000792289606361",
        "Счет 73654108430135874305"
    ]

    print("Результаты маскировки:")
    for card in test_cards:
        print(f"{card} => {mask_account_card(card)}")

    print("\nДата:", get_date("2024-03-11T02:26:18.671407"))


if __name__ == "__main__":
    main()
