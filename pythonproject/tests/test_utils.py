from unittest.mock import patch, Mock
from external_api.api import convert_to_rub

@patch('external_api.api.requests.get')
def test_convert_to_rub(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {'result': 7500.0}  
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'USD'}
        }
    }

    assert convert_to_rub(transaction) == 7500.0
