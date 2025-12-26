from typing import Dict
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculator_3_calculate_success():
    driver_handler = NumpyHandler()
    calculator = Calculator3(driver_handler)

    mock_request = MockRequest({
        "numbers": [2, 4, 6, 8, 10]
    })

    request = mock_request
    response = calculator.calculate(request)

    assert response == {
        "data": {
            "Calculator": 3,
            "variance": 8.0,
            "Success": True
        }
    }

def test_calculator_3_calculate_variance_greater_than_multiplication():
    driver_handler = NumpyHandler()
    calculator = Calculator3(driver_handler)

    mock_request = MockRequest({
        "numbers": [1, 2, 3]
    })

    request = mock_request
    with raises(ValueError, match="Variance is greater than multiplication"):
        calculator.calculate(request)