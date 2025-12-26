from typing import Dict, List
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_inteface import DriverHandlerInterface


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        mean_value = self.__driver_handler.mean(input_data)
        response = self.__format_response(mean_value)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if not body or 'numbers' not in body:
            raise ValueError("Missing 'numbers' in request body")
        input_data = body['numbers']
        if not isinstance(input_data, list) or not all(isinstance(x, (int, float)) for x in input_data):
            raise ValueError("'numbers' must be a list of numbers")
        if len(input_data) == 0:
            raise ValueError("'numbers' must not be empty")
        return input_data

    def __format_response(self, mean_value: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(mean_value, 2)
            }
        }

