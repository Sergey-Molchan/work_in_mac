import os
import requests
from dotenv import load_dotenv
from typing import Dict

load_dotenv()


def convert_to_rub(transaction: Dict) -> float:
    try:
        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']['code']
    except KeyError:
        raise ValueError("Некорректная транзакция")

    if currency == 'RUB':
        return float(amount)

    api_key = os.getenv('EXCHANGE_API_KEY')
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {
        'from': currency,
        'to': 'RUB',
        'amount': amount
    }
    headers = {'apikey': api_key}

    response = requests.get(url, headers=headers, params=params, timeout=10)

    # Обработка ошибок
    if response.status_code != 200:
        error_info = response.json().get('error', 'Неизвестная ошибка')
        raise ValueError(f"Ошибка API ({response.status_code}): {error_info}")

    result = response.json().get('result')
    if not result:
        raise ValueError("Не удалось получить результат конвертации")

    return round(result, 2)
