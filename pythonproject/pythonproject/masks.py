def mask_card(number: str) -> str:
    # Удаляем все нецифровые символы
    cleaned = ''.join(filter(str.isdigit, number))
    if len(cleaned) != 16:
        raise ValueError("Некорректный номер карты")
    return f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"


def mask_account(number: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры."""
    if len(number) < 4 or not number.isdigit():
        raise ValueError("Некорректный номер счета")
    return f"**{number[-4:]}"
