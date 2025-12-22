from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
   calc = Calculator1()
   try:
      response = calc.calculate(request)
      return jsonify(response), 200
   except ValueError as e:
      return jsonify({"error": str(e)}), 400
   except Exception:
      return jsonify({"error": "Internal server error"}), 500