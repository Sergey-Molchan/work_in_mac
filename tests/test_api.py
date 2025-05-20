from unittest.mock import patch
import pytest
from typing import Dict
from external_api.api import convert_to_rub


def test_convert_to_rub_success():
    transaction: Dict = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'USD'}
        }
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'result': 7500.50}
        assert convert_to_rub(transaction) == 7500.50