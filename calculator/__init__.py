'''

This Python code defines a Calculator class with high functionality.

'''

# Import necessary modules and classes
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
         """
        Create and perform a calculation, then return the result.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.
            operation (Callable): A callable representing the operation (add, subtract, etc.).

        Returns:
            Decimal: The result of the calculation.
        """
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        # Perform addition by delegating to the _perform_operation method with the add operation
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        # Perform subtraction by delegating to the _perform_operation method with the subtract operation
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        # Perform multiplication by delegating to the _perform_operation method with the multiply operation
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        # Perform division by delegating to the _perform_operation method with the divide operation
        return Calculator._perform_operation(a, b, divide)