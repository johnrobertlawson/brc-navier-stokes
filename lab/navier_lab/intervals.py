"""Minimal outward-rounded decimal intervals.

This is a seed for small independent certificate verifiers. It intentionally offers only
basic arithmetic and is not a replacement for a mature interval package.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from typing import Self


def _decimal(value: str | int | Decimal) -> Decimal:
    if isinstance(value, float):
        raise TypeError("construct intervals from strings, ints, or Decimals, not floats")
    return value if isinstance(value, Decimal) else Decimal(value)


def _op(a: Decimal, b: Decimal, operation: str, rounding: str) -> Decimal:
    with localcontext() as context:
        context.rounding = rounding
        if operation == "add":
            return a + b
        if operation == "subtract":
            return a - b
        if operation == "multiply":
            return a * b
        if operation == "divide":
            return a / b
    raise ValueError(f"unknown operation {operation}")


@dataclass(frozen=True)
class Interval:
    lower: Decimal
    upper: Decimal

    def __init__(
        self,
        lower: str | int | Decimal,
        upper: str | int | Decimal | None = None,
    ) -> None:
        low = _decimal(lower)
        high = low if upper is None else _decimal(upper)
        if low > high:
            raise ValueError("interval lower endpoint exceeds upper endpoint")
        object.__setattr__(self, "lower", low)
        object.__setattr__(self, "upper", high)

    @property
    def width(self) -> Decimal:
        return _op(self.upper, self.lower, "subtract", ROUND_CEILING)

    def contains(self, value: str | int | Decimal) -> bool:
        point = _decimal(value)
        return self.lower <= point <= self.upper

    def contains_zero(self) -> bool:
        return self.lower <= 0 <= self.upper

    def __add__(self, other: Self) -> Self:
        return type(self)(
            _op(self.lower, other.lower, "add", ROUND_FLOOR),
            _op(self.upper, other.upper, "add", ROUND_CEILING),
        )

    def __sub__(self, other: Self) -> Self:
        return type(self)(
            _op(self.lower, other.upper, "subtract", ROUND_FLOOR),
            _op(self.upper, other.lower, "subtract", ROUND_CEILING),
        )

    def __mul__(self, other: Self) -> Self:
        lower_products = [
            _op(a, b, "multiply", ROUND_FLOOR)
            for a in (self.lower, self.upper)
            for b in (other.lower, other.upper)
        ]
        upper_products = [
            _op(a, b, "multiply", ROUND_CEILING)
            for a in (self.lower, self.upper)
            for b in (other.lower, other.upper)
        ]
        return type(self)(min(lower_products), max(upper_products))

    def reciprocal(self) -> Self:
        if self.contains_zero():
            raise ZeroDivisionError("cannot invert an interval containing zero")
        return type(self)(
            _op(Decimal(1), self.upper, "divide", ROUND_FLOOR),
            _op(Decimal(1), self.lower, "divide", ROUND_CEILING),
        )

    def __truediv__(self, other: Self) -> Self:
        return self * other.reciprocal()

    def __str__(self) -> str:
        return f"[{self.lower}, {self.upper}]"
