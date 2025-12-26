from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body = {"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
    
    # Response format check
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Response assertions
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_invalid_body():
    mock_request = MockRequest(body = {"num": 1})
    calculator_1 = Calculator1()

    with raises(ValueError) as e:
        calculator_1.calculate(mock_request)
    assert str(e.value) == "Missing 'number' in request body"