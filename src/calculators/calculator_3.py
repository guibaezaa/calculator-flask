from typing import Dict, List
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_inteface import DriverHandlerInterface


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)
        formated_response = self.__format_response(variance)
        return formated_response
        
    def __validate_body(self, body: Dict) -> List[float]:
        if not body or 'numbers' not in body:
            raise ValueError("Missing 'numbers' in request body")
        input_data = body['numbers']
        if not isinstance(input_data, list) or not all(isinstance(x, (int, float)) for x in input_data):
            raise ValueError("'numbers' must be a list of numbers")
        return input_data
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        product = 1
        for number in numbers:
            product *= number
        return product
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance > multiplication:
            raise ValueError("Variance is greater than multiplication")         
          
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "variance": variance,
                "Success": True
            }
        }