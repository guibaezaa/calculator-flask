from typing import Dict
from pytest import raises
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"numbers": [2, 4, 6]})
    driver = NumpyHandler()
    calculator = Calculator4(driver)

    response = calculator.calculate(mock_request)
    
    # Response format check
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Response assertions
    assert response["data"]["result"] == 4.0
    assert response["data"]["Calculator"] == 4


def test_calculate_invalid_body():
    mock_request = MockRequest(body={"num": [1, 2]})
    driver = NumpyHandler()
    calculator = Calculator4(driver)

    with raises(ValueError) as e:
        calculator.calculate(mock_request)
    assert str(e.value) == "Missing 'numbers' in request body"
