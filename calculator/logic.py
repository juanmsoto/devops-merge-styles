"""Core arithmetic logic for the calculator."""

from __future__ import annotations


class Calculator:
    """Provide elementary arithmetic operations."""

    def add(self, left: float, right: float) -> float:
        num1 = left
        num2 = right
        return num1 + num2

    def subtract(self, left: float, right: float) -> float:
        return left - right

    def multiply(self, left: float, right: float) -> float:
        return left * right

    def divide(self, left: float, right: float) -> float:
        if right == 0:
            raise ValueError("Division by zero is undefined.")
        return left / right
