from __future__ import annotations

from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_inteface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        formated_response = self.__format_response(calculated_number)
        return formated_response
        
    def __validate_body(self, body: Dict) -> List[float]:
        if not body or 'numbers' not in body:
            raise ValueError("Missing 'numbers' in request body")
        input_data = body['numbers']
        if not isinstance(input_data, list) or not all(isinstance(x, (int, float)) for x in input_data):
            raise ValueError("'numbers' must be a list of numbers")
        return input_data
        
    def __process_data(self, input_data: List[float]) -> float:
        first_processs_result = [(num * 11) ** 0.95 for num in input_data]
        standard_deviation = self.__driver_handler.standard_derivation(first_processs_result)
        final_result = 1/standard_deviation
        return final_result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
            }
        }

        

        