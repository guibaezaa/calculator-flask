from typing import List
import math


class NumpyHandler:
	def standard_derivation(self, numbers: List[float]) -> float:
		if not numbers:
			raise ValueError("'numbers' must be a non-empty list")
		mean = sum(numbers) / len(numbers)
		variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
		return math.sqrt(variance)
